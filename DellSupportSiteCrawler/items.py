# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NetworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    version = scrapy.Field()
    release_date = scrapy.Field()
    last_update = scrapy.Field()
    file_name = scrapy.Field()
    file_size = scrapy.Field()
    file_description = scrapy.Field()
    older_versions = scrapy.Field()
    download_link = scrapy.Field()

