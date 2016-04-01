# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Publication(scrapy.Item):
    title = scrapy.Field()
    # text = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
