# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SpiderResult(scrapy.Item):
    uuid = scrapy.Field()
    result = scrapy.Field()
    page = scrapy.Field()


class SpiderParseResult(scrapy.Item):
    uuid = scrapy.Field()
    type_ = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    nickName = scrapy.Field()


class SpiderCookieItem(scrapy.Item):
    type_ = scrapy.Field()
    isUser = scrapy.Field()
    cookies = scrapy.Field()
    createTime = scrapy.Field()
    username = scrapy.Field()
