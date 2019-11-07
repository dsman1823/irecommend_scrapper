# -*- coding: utf-8 -*-
import scrapy

from irecommend_scrapper import items


class IrecommendSpider(scrapy.Spider):
    name = 'irecommend'
    allowed_domains = ['irecommend.ru']
    start_urls = [
        'https://irecommend.ru/content/khlebopechka-endever-endever-mb-51',
    ]

    def parse(self, response):
        product = items.Product()

        product['title'] = response.css('h1.largeHeader span.fn::text').get()
        product['rating'] = response.css('span.rating::text').get()
        product['amount_of_votes'] = response.css('span.count::text').get()
        description = response.xpath('//div[@itemprop="description"]/*').css('a::text').getall()
        product['category'], product['brand'], product['type'] = list(filter(lambda i: not i.isspace(), description))

        yield product
