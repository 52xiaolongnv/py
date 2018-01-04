# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from yiujob.items import YiujobItem
from scrapy.conf import settings
import pymongo

class YiujobPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbName]
        tdb.authenticate("52xiaolongnv", "#wo$hen%hao_!!")
        self.post1 = tdb[settings['MONGODB_DOCNAME1']]
        # self.post2 = tdb[settings['MONGODB_DOCNAME2']]


    def process_item(self, item, spider):
        # return item
        # pass
        bookInfo = dict(item)
        # if self.post1.find_one() == None:
        self.post1.insert(bookInfo)
        return 'ok '
        # else:
        #     try:
        #         self.post1.update({}, {"$set": bookInfo})
        #         # print('已修改')
        #     except Exception as e:
        #         print('错误')
        #         print(e)

        # try:
        #     self.post1.insert(bookInfo)
        # except Exception as e:
        #     print('错误')
        #     print(e)

