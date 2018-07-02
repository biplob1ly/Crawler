import os
from general import *

class Spider:

    def __init__(self, project_name, base_url, domain):
        self.project_name = project_name
        self.base_url = base_url
        self.domain = domain
        self.queued_file = os.path.join(project_name, "queued.txt")
        self.crawled_file = os.path.join(project_name, "crawled.txt")
        self.queued_link_set = set()
        self.crawled_link_set = set()
        self.boot()



    def boot(self):
        create_dir(self.project_name)
        create_files(self.project_name, self.base_url)
        


    def crawl_page(self, thread_name, page_url):
        if (page_url not in self.crawled_link_set):
            print("Thread " + thread_name + "is crawling " + page_url)
            print("Queued: " + str(len(self.queued_link_set)) + " Crawled: " + str(len(self.crawled_link_set)))
