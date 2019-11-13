import boto3
import pandas as pd

from irecommend_scrapper import items
from irecommend_scrapper import settings


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

    def save_locally(self):
        pd.DataFrame(self.products).to_parquet('data/products.gzip', compression='gzip')
        pd.DataFrame(self.users).to_parquet('data/users.gzip', compression='gzip')
        pd.DataFrame(self.reviews).to_parquet('data/reviews.gzip', compression='gzip')

    def upload_to_s3(selfs):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        s3_client.upload_file('data/products.gzip', settings.BUCKET_NAME, 'products.gzip')
        s3_client.upload_file('data/users.gzip', settings.BUCKET_NAME, 'users.gzip')
        s3_client.upload_file('data/reviews.gzip', settings.BUCKET_NAME, 'reviews.gzip')

    def close_spider(self, spider):
        self.save_locally()
        self.upload_to_s3()
