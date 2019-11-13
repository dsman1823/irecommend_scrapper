from irecommend_scrapper.utils import get_proxies

BOT_NAME = 'irecommend_scrapper'

SPIDER_MODULES = ['irecommend_scrapper.spiders']
NEWSPIDER_MODULE = 'irecommend_scrapper.spiders'

CONCURRENT_REQUESTS = 256
CONCURRENT_REQUESTS_PER_DOMAIN = 256

ROBOTSTXT_OBEY = False

RETRY_HTTP_CODES = [521]
ITEM_PIPELINES = {
    'irecommend_scrapper.pipelines.IrecommendScrapperPipeline': 300,
}



DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 800,
}

ROTATING_PROXY_LIST = get_proxies()

AWS_ACCESS_KEY_ID = "AKIA6K6QFJAG2PDUA6GS"
AWS_SECRET_ACCESS_KEY = "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"
BUCKET_NAME = "spark-lrng-d.sei"

