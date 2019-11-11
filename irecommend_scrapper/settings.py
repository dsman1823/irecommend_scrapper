BOT_NAME = 'irecommend_scrapper'

SPIDER_MODULES = ['irecommend_scrapper.spiders']
NEWSPIDER_MODULE = 'irecommend_scrapper.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 10

ITEM_PIPELINES = {
    'irecommend_scrapper.pipelines.IrecommendScrapperPipeline': 300,
}
