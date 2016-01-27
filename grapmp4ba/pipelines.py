# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from grapmp4ba.model import Movie, DBSession
import time
import cgi
import re


class Grapmp4BaPipeline(object):

    def process_item(self, item, spider):
        detail = cgi.escape('<br>'.join(filter(lambda x: x!='', [x.strip().encode('utf-8', 'ignore') for x in item['detail']])))

        pattern = re.compile('(?<=HD)\d+(?=P)')
        pattern2 = re.compile('(?<==)\w+')

        definition = pattern.match(item['title']).group() if pattern.match(item['title']) else None
        hashcode = pattern2.match(item['link']).group() if pattern2.match(item['link']) else None
        
        movie = Movie(title=item['title'],
                      date_id=time.strftime('%Y%m%d'),
                      link=item['link'],
                      definition=definition,
                      pic_path=item['pic_path'],
                      dl_link=item['dl_link'],
                      detail=detail,
                      hashcode=hashcode
                      )
        try:
            self.session.add(movie)
            self.session.commit()
        except Exception, e:
            print e
            raise e
        

    def open_spider(self, spider):
        self.session = DBSession()

    def close_spider(self, spider):
        self.session.close()
