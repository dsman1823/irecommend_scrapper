import pandas as pd

from irecommend_scrapper import items


class IrecommendScrapperPipeline(object):

    def __init__(self):
        super().__init__()
        self.products = []
        self.reviews = []
        self.users = []

    def process_item(self, item, spider):
        if isinstance(item, items.ProductItem):
            self.products.append(item)
        if isinstance(item, items.ReviewItem):
            self.reviews.append(item)
        if isinstance(item, items.UserItem):
            self.users.append(item)

    def close_spider(self, spider):
        pd.DataFrame(self.products).to_parquet('/home/ITRANSITION.CORP/d.sey/tmp/products.gzip', compression='gzip')
        pd.DataFrame(self.users).to_parquet('/home/ITRANSITION.CORP/d.sey/tmp/users.gzip', compression='gzip')
        pd.DataFrame(self.reviews).to_parquet('/home/ITRANSITION.CORP/d.sey/tmp/reviews.gzip', compression='gzip')
