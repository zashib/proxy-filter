from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def clear_proxy():
    '''Remove dublicate proxy'''
    proxy_list = []
    with open('proxy_list.txt', 'r') as f:
        proxy_list = [x for x in f.read().splitlines()]
        proxy_list = list(set(proxy_list))
    with open('proxy_list.txt', 'w') as file:
        file.write('\n'.join(proxy_list))

clear_proxy()

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
process.crawl('proxy_filter', domain='yandex.ru')
process.start() # the script will block here until the crawling is finished
