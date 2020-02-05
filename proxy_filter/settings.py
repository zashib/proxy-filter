# -*- coding: utf-8 -*-

##################
#Default settings#
##################

SPIDER_MODULES = ['proxy_filter.spiders']
NEWSPIDER_MODULE = 'proxy_filter.spiders'
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
LOG_LEVEL = 'INFO'
DUPEFILTER_DEBUG = True
DOWNLOAD_TIMEOUT = 5
LOG_ENABLED = False
#USER_AGENT = 'proxy_filter (+http://www.yourdomain.com)'
CONCURRENT_REQUESTS = 128
#DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 128
#CONCURRENT_REQUESTS_PER_IP = 16
#TELNETCONSOLE_ENABLED = False
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
#SPIDER_MIDDLEWARES = {
#    'proxy_filter.middlewares.TutorialSpiderMiddleware': 543,
#}
#DOWNLOADER_MIDDLEWARES = {
#    'proxy_filter.middlewares.TutorialDownloaderMiddleware': 543,
#}
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
#ITEM_PIPELINES = {
#    'proxy_filter.pipelines.TutorialPipeline': 300,
#}
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

###########################
#Rotating proxies settings#
###########################
# https://github.com/TeamHG-Memex/scrapy-rotating-proxies

DOWNLOADER_MIDDLEWARES = {
'proxy_filter.middlewares.RotatingProxyMiddleware': 610,
'proxy_filter.middlewares.BanDetectionMiddleware': 620
}
ROTATING_PROXY_LIST_PATH = 'proxy_list.txt'

ROTATING_PROXY_PAGE_RETRY_TIMES = 1
ROTATING_PROXY_BACKOFF_BASE = 3000000
ROTATING_PROXY_BACKOFF_CAP = 3000000

############
#CSV output#
############

FEED_FORMAT = "csv"
FEED_EXPORT_ENCODING = "utf-8"
FEED_URI = "proxy_filter %(time)s.csv"
FEED_EXPORT_FIELDS = ['proxy', 'latency']
