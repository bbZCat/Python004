# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    cid = scrapy.Field()
    updatetime = scrapy.Field()
    user = scrapy.Field()
    star = scrapy.Field()
    title = scrapy.Field()
    short = scrapy.Field()
    
