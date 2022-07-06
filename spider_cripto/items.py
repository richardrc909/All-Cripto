# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags
from scrapy_djangoitem import DjangoItem
from allcripto.models import Bitcoin, Ethereum, MetaVerse, Tutorial, Prices, Business


def remove_space(value):
    return value.replace('\n', '').replace('\xa0', '').replace('/', '').replace('news', '').strip()



class CriptoItem(DjangoItem):
    django_model = Bitcoin
    # django_model = Ethereum
    # django_model = MetaVerse
    # django_model = Tutorial
    # django_model = Prices
    # django_model = Business
    # django_model = AnchorNews
    title = Field(input_processor= MapCompose(remove_tags, remove_space), output_processor = TakeFirst())
    header = Field(input_processor= MapCompose(remove_tags, remove_space), output_processor = TakeFirst())
    paragraph = Field(input_processor= MapCompose(remove_tags, remove_space), output_processor=TakeFirst())


class CriptoAnchor(Item):
    anchor = Field()