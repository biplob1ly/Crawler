from urllib.parse import urlparse


def get_domain_name(url):
    try:
        results = get_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''