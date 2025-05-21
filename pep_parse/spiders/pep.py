import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for link in response.css(
            'td:nth-child(2) a.pep::attr(href)'
        ).getall()[:]:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_number, name = (
            (response.css('h1.page-title::text').get()).split(' – ')
        )
        yield PepParseItem(
            number=pep_number.replace('PEP ', ''),
            name=name,
            status=response.css(
                'dt:contains(\'Status\') + dd abbr::text'
            ).get()
        )
