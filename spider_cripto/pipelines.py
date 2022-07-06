# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class SpiderCriptoPipeline(object):

    def process_item(self, item, spider):
        item.save()


class CriptoAnchorPipeline():

    def __init__(self) -> None:
        self.con = sqlite3.connect('allcripto.db')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):

        # datos_bit = self.cur.execute(""" INSERT INTO allcripto_anchor_bit (anchor_bit) VALUES(?)""",
        #                  (item['anchor']))
        # datos_eth = self.cur.execute(""" INSERT INTO allcripto_anchor_eth (anchor_eth) VALUES(?)""",
        #                  (item['anchor']))
        # datos_meta = self.cur.execute(""" INSERT INTO allcripto_anchor_meta (anchor_meta) VALUES(?)""",
        #                  (item['anchor']))
        # datos_tutorial = self.cur.execute(""" INSERT INTO allcripto_anchor_tutorial (anchor_tutorial) VALUES(?)""",
        #                  (item['anchor']))
        # datos_prices = self.cur.execute(""" INSERT INTO allcripto_anchor_prices (anchor_prices) VALUES(?)""",
        #                  (item['anchor']))
        # datos_business = self.cur.execute(""" INSERT INTO allcripto_anchor_business (anchor_business) VALUES(?)""",
        #                  (item['anchor']))
        self.con.commit()
        return item
