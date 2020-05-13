# -*- coding: utf-8 -*-
import scrapy


class ImagespiderSpider(scrapy.Spider):
    name = 'imagespider'
    allowed_domains = ['books.com']
    start_urls = ['http://books.com/']

    def parse(self, response):
        pass
