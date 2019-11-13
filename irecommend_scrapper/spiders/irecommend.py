# -*- coding: utf-8 -*-
import re

import scrapy

from irecommend_scrapper import items


class IrecommendSpider(scrapy.Spider):
    name = 'irecommend'
    allowed_domains = ['irecommend.ru']
    start_urls = [
        'https://irecommend.ru/category/dlya-kukhni'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse_amount_of_reviews_str(reviews_str):
        return re.sub("[^0-9]", "", str(reviews_str))

    def parse_user(self, response):
        user = items.UserItem()
        user['username'] = response.css('div.user-name::text').get()
        user['participation_time'] = response.css('dd::text').get()
        amount_of_reviews_str = response.css('div.breadcrumb a::text').get()
        user['amount_of_reviews'] = IrecommendSpider.parse_amount_of_reviews_str(amount_of_reviews_str)
        yield user

    def parse_review(self, response):
        user_selector = response.xpath('//strong[@class="reviewer"]/*').css('a')

        review = items.ReviewItem()
        review['title'] = response.xpath('//h2[@itemprop="name"]/*').css('a').css('::text').get()
        review['user'] = user_selector.css('::text').get()
        review['published_at'] = response.css('span.dtreviewed::text').get()
        review['cons'] = response.css('div.plus li::text').getall()
        review['pros'] = response.css('div.minus li::text').getall()
        review['does_recommend'] = response.css('span.verdict::text').get()
        review['body'] = response.css('div.reviewText').get()

        yield review
        yield response.follow(user_selector.css('::attr(href)').get(), callback=self.parse_user)

    def parse_reviews(self, response):
        review_hrefs = response.css('a.more::attr(href)').getall()
        for r in review_hrefs:
            yield response.follow(r, callback=self.parse_review)

    def parse_product(self, response):
        product = items.ProductItem()
        product['title'] = response.css('h1.largeHeader span.fn::text').get()
        product['rating'] = response.css('span.rating::text').get()
        product['amount_of_votes'] = response.css('span.count::text').get()
        product['category'] = response.css('div.vid-1 a::text').get()
        product['brand'] = response.css('div.vid-2 a::text').get()
        product['type'] = response.css('div.vid-55 a::text').get()

        yield product

        reviews_pages_selector = response.css('li.pager-last a::text').get()
        amount_of_pages = int(reviews_pages_selector) if reviews_pages_selector else 1
        for i in range(0, amount_of_pages):
            yield response.follow(response.url + '?page=' + str(i), callback=self.parse_reviews)


def parse_page(self, response):
    for ref in response.css('div.title a::attr(href)').getall():
        yield response.follow(ref, callback=self.parse_product)


def parse(self, response):
    amount_of_pages = int(response.css('li.pager-last a::text').get())
    for i in range(0, amount_of_pages):
        yield response.follow('/category/dlya-kukhni?page=' + str(i), callback=self.parse_page)
