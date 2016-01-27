# -*- coding: utf-8 -*-
# 
import scrapy
import time
import re
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from grapmp4ba.items import Mp4BaItem

today = time.strftime('%m/%d')

class MovieSpider(scrapy.Spider):
    name = 'mp4ba'
    allowed_domains = ["www.mp4ba.com"]
    start_urls = [
        "http://www.mp4ba.com/index.php?sort_id=2",
        "http://www.mp4ba.com/index.php?sort_id=3"
    ]

    def parse(self, response):

        date_path = '//table[@id="listTable"]/tbody/tr/td[1]/text()'
        title_path = '//table[@id="listTable"]/tbody/tr[%s]/td[3]/a/text()'
        link_path = '////table[@id="listTable"]/tbody/tr[%s]/td[3]/a/@href'
        rs = response.xpath(date_path).extract()
        for index, item in enumerate(rs):
            date = item.split(' ')[0]
            if date == today:
                title = response.xpath(title_path%(index+1)).extract()
                link = 'http://' + self.allowed_domains[0] + '/' + response.xpath(link_path%(index+1)).extract()[0]
                yield Request(url=link,dont_filter=True,callback=self.parse_detail)




    def parse_detail(self, response):
        """grab detail"""

        title_path = '//div[@class="location"]/text()[3]'
        pic_path = '//div[@class="intro"]/img/@src'
        detail_path = '//div[@class="intro"]/text()' 
        dl_link_path = '//p[@class="original download"/a/@href' 
        detail_path = '///div[@class="intro"]/text()'      
        print response.body
        item = Mp4BaItem()
        pattern = re.compile(r'(?<=HD)\d+(?=P)')
        pattern2 = re.compile(r'(?<=hash\=)\w+')
        item['title'] = response.xpath(title_path).extract()[0].encode('utf-8','ignore')
        item['link'] = response.url
        item['definition'] = pattern.match(item['title']).group() if pattern.match(item['title']) else None
        item['pic_path'] = response.xpath(pic_path).extract()[0]
        item['dl_link'] = response.xpath(dl_link_path).extract()[0]
        item['detail'] = '<br>'.join([x.encode('uft-8') for x in response.xpath(detail_path).extract()])
        item['hashcode'] = pattern.match(response.url).group()

        yield item