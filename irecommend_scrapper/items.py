# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    amount_of_votes = scrapy.Field()
    category = scrapy.Field()
    brand = scrapy.Field()
    type = scrapy.Field()


class Review(scrapy.Item):
    title = scrapy.Field()
    user = scrapy.Field()
    published_at = scrapy.Field()
    body = scrapy.Field()
    pros = scrapy.Field()
    cons = scrapy.Field()
    does_recommend = scrapy.Field()


class User(scrapy.Item):
    username = scrapy.Field()
    participation_time = scrapy.Field()
    amount_of_reviews = scrapy.Field()
