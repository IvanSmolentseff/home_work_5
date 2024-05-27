# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksparserItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    translator = scrapy.Field()
    url = scrapy.Field()
    general_price = scrapy.Field()
    your_price = scrapy.Field()
    currency = scrapy.Field()
    _id = scrapy.Field()