import scrapy
import re
import time
from datetime import datetime
from scrapy.selector import Selector

from douban_spider.items import DoubanSpiderItem
#from douban_spider.piplines import 

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['douban.com']
    
    def start_requests(self):
        start_url = 'https://movie.douban.com/subject/30346025/reviews?start='
        for i in range(5):
            yield scrapy.Request(url=f"{start_url}{i*20}", callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(f'Processing {response.request.url}')

        item = DoubanSpiderItem()

        commentlist = Selector(response=response).xpath('//div[@class="review-list  "]/div')
        for comm in commentlist:
            cid = comm.xpath('./@data-cid').get()
            user = comm.xpath('./div/header/a[2]/text()').get()
            updatetime = comm.xpath('./div/header/span[2]/text()').get()
            star = comm.xpath('./div/header/span[1]/@class').get()
            title = comm.xpath('./div/div/h2/a/text()').get()
            
            shorts = comm.xpath('./div/div/div/div/text()').getall()
            shortfull = ''
            for short in shorts:
                shortfull += short.strip()
            shortfull = shortfull[:-7].strip()
            #print(f"{cid} : {shortfull} -END-")

            item['cid'] = int(cid)
            item['user'] = user 
            item['updatetime'] = updatetime
            #print(star)
            if star[:7] == 'allstar':
                item['star'] = int(star[7:8])
            else:
                item['star'] = 0
                
            item['title'] = title 
            item['short'] = shortfull

            #print(item)
            yield item

        
