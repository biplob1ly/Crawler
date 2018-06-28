from general import *

PROJECT_NAME = "planetebook"
BASE_URL = "https://www.planetebook.com/"
QUEUED_FILE = os.path.join(PROJECT_NAME, "queued.txt")
CRAWLED_FILE = os.path.join(PROJECT_NAME, "crawled.txt")

create_dir(PROJECT_NAME)
create_files(PROJECT_NAME, BASE_URL)
