# -*- coding: utf-8 -*-
import scrapy
class DoubanItem(scrapy.Item):
    movieRank = scrapy.Field()
    movieName = scrapy.Field()
    moviePic = scrapy.Field()
    starNum = scrapy.Field()
    quoteNum = scrapy.Field()
    movieDes = scrapy.Field()
