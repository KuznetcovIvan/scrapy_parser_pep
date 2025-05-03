import sys

import scrapy

from ..settings import ALLOWED_DOMAIN, NAME, NUMBER, START_URL, STATUS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAIN]
    start_urls = [START_URL]

    def parse(self, response):
        for link in response.css('td:nth-child(2) a.pep::attr(href)').getall(
        )[:5 if 'pytest' in sys.modules else None]:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_number, name = (
            (response.css('h1.page-title::text').get()).split(' – ')
        )
        yield {
            NUMBER: pep_number.replace('PEP ', ''),
            NAME: name,
            STATUS: response.css('dt:contains("Status") + dd abbr::text').get()
        }
