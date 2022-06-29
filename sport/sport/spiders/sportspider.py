import scrapy
from sport.items import SportItem
import time

class SportspiderSpider(scrapy.Spider):
    name = 'sportspider'
    allowed_domains = ['sportsv.net']
    start_urls = ['http://sportsv.net/']

    def parse(self, response):
        posts = response.css('.item_lish')
        dates = posts.xpath('//div[@class= "row item"]/div[@class="col-md-6"]/div[@class="date"]/text()').getall()
        authors = posts.xpath('//div[@class= "row item"]/div[@class="col-md-6"]/div[@class="author"]/a[@class="author_name"]/text()').getall()
        titles = posts.xpath('//div[@class= "row item"]/div[@class="col-md-6"]/h4/a/text()').getall()
        print(dates)
        print('----')
        print(authors)
        print('-----')
        print(titles)
        print(len(dates),len(authors),len(titles))
        # next_page = response.xpath('//div[@class="pagination"]/ul/li/a/@href').getall()[5]
        for i in range(len(dates)) :
                item = SportItem()
                date = dates[i]
                author = authors[i]
                title = titles[i]
                item['date'] = date
                item['author'] = author
                item['title'] = title
                print(date,author,title)
                yield item
                
        # print(next_page)
        # # 讓爬蟲可以暫停休息幾秒繼續，避免太暴力爬取網站造成網站負擔
        # time.sleep(3)
        # # 讓爬蟲可以繼續發出網路請求爬取下一頁資料並解析內容
        # yield response.follow(next_page,  self.parse)