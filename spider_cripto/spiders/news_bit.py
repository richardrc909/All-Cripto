import scrapy
import sqlite3
from scrapy import Spider
from bs4 import BeautifulSoup
from scrapy.loader import ItemLoader
from spider_cripto.items import CriptoItem

""" Esta variable en el final usa un {} para que la url sea dinámica en el sitio donde extraigo las noticias
    no existe un pátron que sea utilizable que me permita extraer todo el cuerpo de las noticias"""

base_url = 'https://es.cointelegraph.com{}'


class BitcoinSpider(Spider):
    """ Inicializando la funcion con sus configuraciones iniciales: nombre(el que eligas),
        custom settings y el diccionario con el user agent que nos servirá de mascara por decirlo
        así en la petición que hará el spider, de esta manera y siguiendo las ordenes del archivo.txt
        podemos evitar que nos baneen la ip por peticiones """


    name = "bitcoineta"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    download_delay = 2

    def start_requests(self):
        con = sqlite3.connect('allcripto.db')
        con.row_factory = lambda cursor, row:row[0]
        c = con.cursor()
        datos = c.execute("SELECT anchor_bit FROM allcripto_anchor_bit").fetchall()
        for partial_link in datos:
            yield scrapy.Request(base_url.format(partial_link))

    def parse(self, response):
        soup = BeautifulSoup(response.body, features='lxml')
        title = soup.find('h1', 'post__title').text
        header = soup.find('p', 'post__lead').text
        content = soup.find('div',class_="post-content").text
        item = ItemLoader(CriptoItem())
        item.add_value('title', title)
        item.add_value('header', header)
        item.add_value('paragraph', content)
        yield item.load_item()
            