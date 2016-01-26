# -*- coding: utf-8 -*-
# 
import scrapy

class MovieSpider(scrapy.Spider):
    name = 'mp4ba'
    start_url = [
        'http://www.mp4ba.com/index.php?sort_id=2',
        'http://www.mp4ba.com/index.php?sort_id=3'
    ]

    def parse(self, response):
        filename = 'mp4ba'
        print 'right here'
        with open(filename, 'wb') as f:
            f.write(response.body)