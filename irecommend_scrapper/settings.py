from irecommend_scrapper.utils import get_proxies

BOT_NAME = 'irecommend_scrapper'

SPIDER_MODULES = ['irecommend_scrapper.spiders']
NEWSPIDER_MODULE = 'irecommend_scrapper.spiders'

CONCURRENT_REQUESTS = 256
CONCURRENT_REQUESTS_PER_DOMAIN = 256

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'irecommend_scrapper.pipelines.IrecommendScrapperPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

ROTATING_PROXY_LIST = get_proxies()
