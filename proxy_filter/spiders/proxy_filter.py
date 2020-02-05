import scrapy
from proxy_filter.items import ProxyFilterItem

def create_urls():
    '''Create list of start urls'''
    with open('proxy_list.txt', 'r') as f:
        # proxy_list = [x for x in f.read().splitlines()]
        return ['https://yandex.ru/internet/' for x in f.read().splitlines()]

def filter_proxy(proxy):
    '''Save filtered proxy to txt file'''
    with open('filtered_proxy_list.txt', 'a') as f:
        f.write(proxy + '\n')

class ProxyFilterSpider(scrapy.Spider):
    name = 'proxy_filter'
    allowed_domains = ['yandex.ru']
    start_urls = create_urls()

    def parse(self, response):
        item = ProxyFilterItem()
        response_ip = response.xpath('/html/body/div[1]/div[1]/div[1]/div[1]/section[1]/ul/li[1]/div[2]/text()').get()
        if response_ip == response.meta['proxy'].split(':')[1][2:]:
            filter_proxy(response.meta['proxy'][7:])
            item['proxy'] = response.meta['proxy']
            item['latency'] = response.meta['download_latency']
            yield item
