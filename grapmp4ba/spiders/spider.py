# -*- coding: utf-8 -*-
# 
import scrapy

class MovieSpider(scrapy.Spider):
    name = 'mp4ba'
    allowed_domains = ["www.mp4ba.com"]
    start_url = [
        "http://www.mp4ba.com/index.php?sort_id=2",
        "http://www.mp4ba.com/index.php?sort_id=3"
    ]

    def parse(self, response):
        print response.body