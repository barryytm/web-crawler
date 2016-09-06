import scrapy

from crawler.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["calendar.artsci.utoronto.ca"]
    start_urls = [
        "http://calendar.artsci.utoronto.ca/crs_csc.htm"
    ]

    def parse(self, response):
        for sel in response.xpath('//span[contains(@class, "strong")]'):
            course = sel.re('\w{3}\d{3}\w\d')
            # preq = sel.xpath('next()')
            about = sel.xpath('following-sibling::p').extract()
            if (len(course) != 0):
                print(course[0])
                print(about[0])
                # print(preq)
                # item = DmozItem()
                # item['course'] = course
                # yield item
                # prerequisites = sel.xpath('//text()')
