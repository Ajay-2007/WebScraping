# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which



class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['http://www.livecoin.net/en/']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_path = which("chromedriver")
        print(chrome_path)
        driver = webdriver.Chrome(r"C:\Users\d33ps3curity\Downloads\chromedriver_win32\chromedriver.exe", options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get('https://wwww.livecoin.net/en')

        rur_tab = driver.find_elements_by_xpath('//div[@class="filterPanel___2zFYQ"]/div')
        print('printing debug', rur_tab)
        rur_tab[0].click()
        self.html = driver.page_source

        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath('//div[contains(@class, ReactVirtualized__Table__row tableRow___3EtiS ")]'):
            yield {
                'currency_pair' : currency.xpath('.//div[1]/div/text()').get(),
                'volumne(24h)' : currency.xpath('.//div[2]/div[2]/span/text()').get()
            }
