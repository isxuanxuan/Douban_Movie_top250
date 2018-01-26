# -*- coding: utf-8 -*-

import csv
class DoubanPipeline(object):
    line = ['movieRank','movieName','moviePic','starNum','quoteNum','movieDes']
    def open_spider(self,spider):
        self.f = open('movie250.csv','w',newline='',encoding='utf_8_sig')
        self.writer = csv.DictWriter(self.f,self.line)
        self.writer.writeheader()
    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
    def close_spider(self,spider):
        self.f.close()
