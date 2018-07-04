import os
from general import *
from domain import *
from urllib.request import urlopen
from link_finder import LinkFinder

class Spider:

    project_name = ''
    base_url = ''
    domain = ''
    queued_file = ''
    crawled_file = ''
    queued_link_set = set()
    crawled_link_set = set()

    def __init__(self, project_name, base_url, domain):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain = domain
        Spider.queued_file = os.path.join(project_name, "queued.txt")
        Spider.crawled_file = os.path.join(project_name, "crawled.txt")
        self.boot()
        self.crawl_page("First Thread", base_url)

    def boot(self):
        create_dir(self.project_name)
        create_files(self.project_name, self.base_url)
        Spider.queued_link_set = read_set_from_file(self.queued_file)
        Spider.crawled_link_set = read_set_from_file(self.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_link_set:
            print("Thread " + thread_name + " is crawling " + page_url)
            print("Queued: " + str(len(Spider.queued_link_set)) + " Crawled: " + str(len(Spider.crawled_link_set)))
            Spider.add_to_link_set(Spider.gather_links(page_url))
            Spider.queued_link_set.remove(page_url)
            Spider.crawled_link_set.add(page_url)
            Spider.update_files()

    @staticmethod
    def add_to_link_set(links):
        for link in links:
            if (link in Spider.queued_link_set) or (link in Spider.crawled_link_set):
                continue
            if get_domain_name(link) != Spider.domain:
                continue
            Spider.queued_link_set.add(link)

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def update_files():
        write_set_to_file(Spider.queued_file, Spider.queued_link_set)
        write_set_to_file(Spider.crawled_file, Spider.crawled_link_set)