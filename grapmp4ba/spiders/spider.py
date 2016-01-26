# -*- coding: utf-8 -*-
# 
import scrapy
import time
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log

today = time.strftime('%m/%d')

class MovieSpider(scrapy.Spider):
    name = 'mp4ba'
    allowed_domains = ["www.mp4ba.com"]
    start_urls = [
        "http://www.mp4ba.com/index.php?sort_id=2",
        "http://www.mp4ba.com/index.php?sort_id=3"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        date_path = '//table[@id="listTable"]/tbody/tr/td[1]/text())'
        title_path = '/table[@id="listTable"]/tbody/tr[%s]/td[3]/a/text())'
        rs = hxs.xpath(date_path).extract()
        for index, item in enumerate(rs):
            date = item.split(' ')[0]
            if date == today:
                title = hxs.xpath(title_path%(index+1)).extract()




    def parse_detail(self, response):
        """grap"""
        pass


def check_exists(title):
    """query from db, to find out if title has been processed"""

    pass