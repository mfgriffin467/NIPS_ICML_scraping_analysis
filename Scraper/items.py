# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NipsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 #   year = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    abstract = scrapy.Field()
    event_type = scrapy.Field()
    year = scrapy.Field()


