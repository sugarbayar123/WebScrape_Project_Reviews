import scrapy
import time

start = time.time()

class ConcertsInfo(scrapy.Item):

    Performer = scrapy.Field()
    Venue = scrapy.Field()
    Address = scrapy.Field()
    Date = scrapy.Field()
    Genre = scrapy.Field()


class ConcertinfoSpider(scrapy.Spider):
    name = "concertInfo"
    allowed_domains = ["https://concertful.com/"]
    try:
        with open("concertlist.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []


    def parse(self, response):
        r = ConcertsInfo()

        Performer_xpath = '//span[@class = "performers"]//a/abbr/text()'
        Venue_xpath = '//span[@class = "venue_name"]/text()'
        Address_xpath = '//th[text()="Venue:"]/following-sibling::td[@class="event_info"]//span[@class="address"]//text()[normalize-space() and not(contains(., ", ")) and not(contains(., ","))]'
        Date_xpath = '//th[contains(text(),"Date:")]/following-sibling::td[@class="event_info"]//text()'
        Genre_xpath = '//th[contains(text(),"Genre:")]/following-sibling::td//text()'



        r['Performer'] = response.xpath(Performer_xpath).getall()
        r['Venue'] = response.xpath(Venue_xpath).getall()
        r['Address'] = [address.replace('\t', '').replace('\n', '').strip() for address in response.xpath(Address_xpath).extract()]
        r['Date'] = [date.replace('\t', '').replace('\n', '').strip() for date in response.xpath(Date_xpath).extract()]
        r['Genre'] = response.xpath(Genre_xpath).getall()

        yield r

        end = time.time()
        print('Here:', end - start)
