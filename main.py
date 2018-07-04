from general import *
import threading
from spider import Spider
from domain import *
from queue import Queue

PROJECT_NAME = "wcfantasy"
BASE_URL = "https://fantasy.fifa.com"
DOMAIN_NAME = get_domain_name(BASE_URL)
QUEUED_FILE = os.path.join(PROJECT_NAME, "queued.txt")
CRAWLED_FILE = os.path.join(PROJECT_NAME, "crawled.txt")
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, BASE_URL, DOMAIN_NAME)


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()


def worker():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_jobs():
    for link in read_set_from_file(QUEUED_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_link_set = read_set_from_file(QUEUED_FILE)
    if len(queued_link_set) > 0:
        print(str(len(queued_link_set)) + " links in the queue")
        create_jobs()


create_workers()
crawl()