import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import NetworkItem


class SiteSpider(scrapy.Spider):
    name = "site_spider"
    allowed_domains = ["dell.com"]
    start_urls = ["http://www.dell.com/support/home/us/en/19/product-support/product/poweredge-m630/drivers"]

    def parse(self, response):
        view_response = response
        # sel = response.css('.driver-table')
        t = response.xpath('//*[@id="divDriversSection"]/div/table/tbody[1]/tr[1]/td[2]/div/a/span[2]/span/text()').extract()
        # title = sel.xpath('//*[@id="divDriversSection"]/div/table/tbody[1]')
        return response

    def parse_site(self, response):
        pass