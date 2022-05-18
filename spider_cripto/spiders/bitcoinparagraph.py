import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from spider_cripto.items import BodyItem

base_url = 'https://es.cointelegraph.com{}'

def read_csv():
    df = pd.read_csv('newlinks.csv')
    return df['partial_link'].values.tolist()




class BitcoinBody(Spider):
    name = "bitcoinp"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    download_delay = 2

    def start_requests(self):
        for partial_link in read_csv():
            yield scrapy.Request(base_url.format(partial_link))


    def parse(self, response):
        pass
        soup = BeautifulSoup(response.body, features='lxml')
        content = soup.find('div',class_="post-content").text
        item = ItemLoader(BodyItem())
        item.add_value('paragraph', content)
        yield item.load_item()