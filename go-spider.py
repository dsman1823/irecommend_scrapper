import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from irecommend_scrapper import settings
from irecommend_scrapper.spiders.irecommend import IrecommendSpider

process = CrawlerProcess(get_project_settings())
settings.AWS_ACCESS_KEY_ID = sys.argv[1]
settings.AWS_SECRET_ACCESS_KEY = sys.argv[2]
process.crawl(IrecommendSpider)
process.start()
