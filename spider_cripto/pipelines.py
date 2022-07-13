# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class SpiderCriptoPipeline(object):

    """ Junto con scrapy_django_items usando esta clase es que logro guardar datos en base de datos, sin embargo
        este archivo es el último eslabon en la cadena """

    def process_item(self, item, spider):
        item.save()


class CriptoAnchorPipeline():

    """ Inicializando la clase recibe dos funciones:
        def init : a) Usando el modulo de sqlite se establece la conexión a base de datos
                   b) En variable (self.cur) se guarda la función cursor que ejecutará más tarde
                      lo que se desee guardar o la accion a usar """

    def __init__(self) -> None:
        self.con = sqlite3.connect('allcripto.db') 
        self.cur = self.con.cursor()

        """ def process_item: Usando la variable (self.cur) de la funcion anterior se guardan los items
                              o la información necesaria.
                              En las distintas variables llamadas datos lo unico que cambia es la tabla
                              en la que se guardará la información y su correspondiente columna """

        """ Según el zen de Python la función antes mencionada viola el principio de Don't repeat yourself
        o DRY pero hasta ahora es la mejor solución que he encontrado hasta el momento
        Seguiré trabajando en otra solución que no viole este principio """

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
