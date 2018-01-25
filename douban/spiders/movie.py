# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
"""
movieRank
movieName
moviePic 
actor = s
director 
year = sc
country =
movieType
starNum =
quoteNum 
movieDes 
"""

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        for li in response.xpath('//ol[@class="grid_view"]/li'):
            item = DoubanItem()
            item['movieRank'] = li.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movieName'] = li.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['moviePic'] = li.xpath('.//div[@class="pic"]/a/img/@src').extract()[0]
            #item['actor'] = li.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            item['starNum'] = li.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            item['quoteNum'] = li.xpath('.//div[@class="star"]/span[4]/text()').extract()[0]
            if li.xpath('.//p[@class="quote"]/span/text()'):
                item['movieDes'] = li.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').extract()[0]
            yield item

        if response.xpath('//span[@class="next"]/a'):
            nextPage = response.xpath('//span[@class="next"]/a/@href').extract()[0]
            yield response.follow(nextPage, callback=self.parse)


