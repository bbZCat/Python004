import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url = url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        item = SpidersItem()
        count = 0
        movies = Selector(response = response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
            url = f'https://maoyan.com' + movie.xpath('./a/@href').extract_first()
            #print('------------------------------------------------------')
            #print(url)
            if(count<10):
                yield scrapy.Request(url=url, meta={'item':item}, callback=self.parse2)
                count+=1

    def parse2(self, response):
        item = response.meta['item']
        movie_info = Selector(response = response)
        item['film_title'] = movie_info.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()').extract_first()
        item['film_type'] = movie_info.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()').extract_first() 
        item['plan_date'] = movie_info.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract_first()
        #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        #print(item)
        yield item

