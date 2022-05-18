# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class SpiderCriptoPipeline:


    def __init__(self) -> None:
        self.con = sqlite3.connect('allcripto.db')
        self.cur = self.con.cursor()
        self.create_table()


    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS allcripto_bitcoin(
            title TEXT,
            header TEXT
        )""")




    def process_item(self, item, spider):
        self.cur.execute(""" INSERT INTO allcripto_bitcoin (title, header) VALUES(?,?)""",
                         (item['title'][0], item['header'][0]))
        self.con.commit()
        return item


class CriptoBodyPipeline():

    
    def __init__(self) -> None:
        self.con = sqlite3.connect('allcripto.db')
        self.cur = self.con.cursor()
        self.create_table()


    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS allcripto_bitcoinbody(
            paragraph TEXT
        )""")