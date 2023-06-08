import scrapy
import pandas as pd
import time

#page_limit = True

#if page_limit == True:
    #pages = 10
#else: pages = 1

start = time.time()


class Link(scrapy.Item):
    link = scrapy.Field()

class ConcertSpider(scrapy.Spider):
    name = "concert"
    allowed_domains = ["https://concertful.com/"]
    start_urls = ["https://concertful.com/area/poland/"]
    #for i in range(pages):
        #start_urls.append('https://concertful.com/area/poland/' + "/?page=" + str(i))

    def parse(self, response):
        xpath = "//span[@class = 'eventName']/a/@href"

        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = "https://concertful.com" + s.get()

            yield l

        end = time.time()
        print('Here:', end - start)