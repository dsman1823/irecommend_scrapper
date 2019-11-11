# -*- coding: utf-8 -*-
import scrapy

from irecommend_scrapper import items


class IrecommendSpider(scrapy.Spider):
    name = 'irecommend'
    allowed_domains = ['irecommend.ru']
    start_urls = [
        'https://irecommend.ru/content/elektricheskii-chainik-moulinex-by730132',
    ]

    def parse_user(self, response):
        user = items.User()
        # user['username'] = response.css('div.user-name')
        yield user

    def parse_review(self, response):
        # yield response.follow(response.xpath('//h2[@itemprop="name"]/*').css('a').css('::attr(href)'), callback=self.parse_user)

        review = items.Review()
        review['title'] = response.xpath('//h2[@itemprop="name"]/*').css('a').css('::text').get()
        review['user'] = response.xpath('//strong[@class="reviewer"]/*').css('a::text').get()
        review['published_at'] = response.css('span.dtreviewed::text').get()
        review['cons'] = response.css('div.plus li::text').getall()
        review['pros'] = response.css('div.minus li::text').getall()
        review['does_recommend'] = response.css('span.verdict::text').get()
        review['body'] = response.css('div.reviewText').get()

        yield review

    def parse(self, response):
        product = items.Product()
        product['title'] = response.css('h1.largeHeader span.fn::text').get()
        product['rating'] = response.css('span.rating::text').get()
        product['amount_of_votes'] = response.css('span.count::text').get()
        description = response.xpath('//div[@itemprop="description"]/*').css('a::text').getall()
        product['category'], product['brand'], product['type'] = list(filter(lambda i: not i.isspace(), description))

        # yield product

        ref = response.css('a.more::attr(href)').getall()[0]
        yield response.follow(ref, callback=self.parse_review)
