import os


def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def append_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        print("Creating directory: " + dir_name)
        os.makedirs(dir_name)


def create_files(dir_name, base_url):
    queued_file = os.path.join(dir_name, "queued.txt")
    crawled_file = os.path.join(dir_name, "crawled.txt")
    if not os.path.isfile(queued_file):
        print("Creating file: " + queued_file)
        write_file(queued_file, base_url)
    if not os.path.isfile(crawled_file):
        print("Creating file: " + crawled_file)
        write_file(crawled_file, '')


def read_set_from_file(filename):
    link_set = set()
    with open(filename, 'rt') as file:
        for line in file:
            link_set.add(line.replace('\n', ''))
    return link_set


def write_set_to_file(filename, link_set):
    with open(filename, 'w') as file:
        for link in sorted(link_set):
            file.write(link + '\n')