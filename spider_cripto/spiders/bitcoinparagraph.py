import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader, Selector
from bs4 import BeautifulSoup
from spider_cripto.items import BodyItem

class BitcoinBody(Spider):
    name = "bitcoin_anchor"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    download_delay = 2
    start_urls = ['https://es.cointelegraph.com/tags/bitcoin']

    def parse(self, response):
        sel = Selector(response)
        news = sel.css('div.post-card-inline__content')
        for elem in news:
            item = ItemLoader(BitcoinAnchor(), elem)
            item.add_css('anchor', 'a.post-card-inline__title-link::attr(href)')
            yield item.load_item()