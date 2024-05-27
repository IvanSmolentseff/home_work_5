# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import re
from urllib.parse import urlparse

class BooksparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.books_labirint

    def process_item(self, item, spider):
        item['_id'] = re.search(r'(\d+)', urlparse(item['url']).path).group(1)
        item['title'] = item.get('title').split(':')[1].strip()
        item.get('author')
        item.get('translator')
        item['general_price'] = float(item.get('general_price'))
        item['your_price'] = float(item.get('your_price'))
        item['currency'] = item.get('currency').replace('₽', 'RUB')
        item.get('url')
        collections = self.mongo_base[spider.name]
        collections.insert_one(item)
        return item
