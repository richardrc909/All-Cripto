import scrapy
import sqlite3
from scrapy import Spider
from bs4 import BeautifulSoup
from scrapy.loader import ItemLoader
from spider_cripto.items import CriptoItem


base_url = 'https://es.cointelegraph.com{}'


class BitcoinSpider(Spider):
    name = "bitcoineta"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    download_delay = 2

    ''' En start_requests para obtener la información ordenada en las spider, primero extraigo los links 
    y en la variable datos son pasados como una lista iterable para justamente obtener la noticia entera '''

    ''' Las listas que siguen sirven para cambiar los valores de la variable datos según que tipo de noticia
    deseamos obtener '''

    list_tables = ['allcripto_anchor_bit', 
    'allcripto_anchor_eth', 
    'allcripto_anchor_meta', 
    'allcripto_anchor_prices',
    'allcripto_anchor_tutorial',
    'allcripto_anchor_business']

    select_colum = ['anchor_bit',
    'anchor_eth',
    'anchor_meta',
    'anchor_prices',
    'anchor_tutorial',
    'anchor_business']

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
            