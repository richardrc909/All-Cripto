from scrapy import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from spider_cripto.items import SpiderCriptoItem


class BitcoinSpider(Spider):
    name = "bitcoineta"
    start_urls = ["https://es.cointelegraph.com/tags/bitcoin"]

    def parse(self, response):
        sel = Selector(response)
        news = sel.css('div.post-card-inline__content')
        for elem in news:
            item = ItemLoader(SpiderCriptoItem(), elem)
            item.add_css('title', 'span.post-card-inline__title')
            item.add_css('header', 'p.post-card-inline__text')
            yield item.load_item()
            