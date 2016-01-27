# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from grapmp4ba.model import Movie, DBSession
import time
import cgi


class Grapmp4BaPipeline(object):

    def process_item(self, item, spider):
        detail = cgi.escape('<br>'.join(filter(lambda x: x!='', [x.strip().encode('utf-8', 'ignore') for x in item['detail']])))
        title = item['title'].encode('utf-8', 'ignore')
        movie = Movie(title=title,
                      date_id=time.strftime('%y%m%d'),
                      link=item['link'],
                      definition=item['definition'],
                      pic_path=item['pic_path'],
                      dl_link=item['dl_link'],
                      detail=detail,
                      hashcode=item['hashcode']
                      )
        self.session.add(movie)
        self.session.commit()

    def open_spider(self, spider):
        self.session = DBSession()

    def close_spider(self, spider):
        self.session.close()
