# -*- coding: utf-8 -*-
import re

import scrapy

from irecommend_scrapper import items


class IrecommendSpider(scrapy.Spider):
    name = 'irecommend'
    allowed_domains = ['irecommend.ru']
    start_urls = [
        'https://irecommend.ru/content/elektricheskii-chainik-moulinex-by730132',
    ]

    def parse_amount_of_reviews_str(reviews_str):
        return re.sub("[^0-9]", "", str(reviews_str))

    def parse_user(self, response):
        user = items.User()
        user['username'] = response.css('div.user-name::text').get()
        user['participation_time'] = response.css('dd::text').get()
        amount_of_reviews_str = response.css('div.breadcrumb a::text').get()
        user['amount_of_reviews'] = IrecommendSpider.parse_amount_of_reviews_str(amount_of_reviews_str)
        yield user

    def parse_review(self, response):
        user_selector = response.xpath('//strong[@class="reviewer"]/*').css('a')

        review = items.Review()
        review['title'] = response.xpath('//h2[@itemprop="name"]/*').css('a').css('::text').get()
        review['user'] = user_selector.css('::text').get()
        review['published_at'] = response.css('span.dtreviewed::text').get()
        review['cons'] = response.css('div.plus li::text').getall()
        review['pros'] = response.css('div.minus li::text').getall()
        review['does_recommend'] = response.css('span.verdict::text').get()
        review['body'] = response.css('div.reviewText').get()

        yield review
        yield response.follow(user_selector.css('::attr(href)').get(), callback=self.parse_user)

    def parse(self, response):
        product = items.Product()
        product['title'] = response.css('h1.largeHeader span.fn::text').get()
        product['rating'] = response.css('span.rating::text').get()
        product['amount_of_votes'] = response.css('span.count::text').get()
        description = response.xpath('//div[@itemprop="description"]/*').css('a::text').getall()
        product['category'], product['brand'], product['type'] = list(filter(lambda i: not i.isspace(), description))

        yield product

        ref = response.css('a.more::attr(href)').getall()[0]
        yield response.follow(ref, callback=self.parse_review)
