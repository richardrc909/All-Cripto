# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_space(value):
    return value.replace('\n', '').strip()



class SpiderCriptoItem(Item):
    title = Field(input_processor= MapCompose(remove_tags))
    header = Field(input_processor= MapCompose(remove_tags))


class BodyItem(Item):
    paragraph = scrapy.Field(input_processor= MapCompose(remove_tags, remove_space), output_processor=TakeFirst())
