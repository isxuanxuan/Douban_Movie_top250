# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    movieRank = scrapy.Field()
    movieName = scrapy.Field()
    moviePic = scrapy.Field()
    #actor = scrapy.Field()
    #director = scrapy.Field()
    #year = scrapy.Field()
    #country = scrapy.Field()
    #movieType = scrapy.Field()
    starNum = scrapy.Field()
    quoteNum = scrapy.Field()
    movieDes = scrapy.Field()
