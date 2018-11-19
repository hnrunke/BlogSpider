# -*- coding: utf-8 -*-

# Scrapy settings for BlogSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BlogSpider'

SPIDER_MODULES = ['BlogSpider.spiders']
NEWSPIDER_MODULE = 'BlogSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'BlogSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     #   'Accept-Language': 'en',
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch, br",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Cache-Control": "no-cache",
#     "Connection": "keep-alive",
#     "Host": "weibo.com",
#     "Pragma": "no-cache",
#     "Upgrade-Insecure-Requests": "1",
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'BlogSpider.middlewares.BlogspiderSpiderMiddleware': 543,
# }
# params = dict()
# with open('.env') as r:
#     lines = r.read().split('\n')
#     for line in lines:
#         param = line.split('=')
#         params[param[0]] = param[-1]
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
REDIS_START_URLS_KEY = '%(name)s:start_urls'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# PriorityQueue（有序集合），FifoQueue（列表）、LifoQueue（列表）
# SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"
# SCHEDULER_PERSIST = True
# SCHEDULER_FLUSH_ON_START = False
# SCHEDULER_IDLE_BEFORE_CLOSE = 10
# SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
# SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# REDIS_URL = f'redis://{params.get("redis_user")}:{params.get("redis_passwd")}@{params.get("redis_ip")}:{params.get("redis_port")}'

REDIS_URL = 'redis://user:123456@192.168.1.111:6379'
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 123,
    #     'BlogSpider.middlewares.IpPools': 124,
    #     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 125,
    #     'BlogSpider.middlewares.UserAgentPools': 126,
    'BlogSpider.middlewares.CookiePools': 127
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {'BlogSpider.pipelines.SpiderResultPipeline': 300}
ITEM_PIPELINES = {'scrapy_redis.pipelines.RedisPipeline': 100}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
