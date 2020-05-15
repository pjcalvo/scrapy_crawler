from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field
from dynaconf import settings

report_if=settings.REPORT_IF


class MyItems(Item):
    referer =Field()
    status = Field()
    response= Field()

class MySpider(CrawlSpider):
    name = settings.NAME
    target_domains = settings.ALLOWED_DOMAINS
    start_urls = settings.START_URLS

    handle_httpstatus_list = [404,410,301,500] # only 200 by default. you can add more status to list

    # Throttle crawl speed to prevent hitting site too hard
    custom_settings = {
        'CONCURRENT_REQUESTS': settings.CONCURRENT_REQUESTS_PER_DOMAIN,
        # Delay in seconds between requests
        'DOWNLOAD_DELAY': settings.DOWNLOAD_DELAY
    }

    rules = [
        Rule(
            LinkExtractor(
                allow_domains=target_domains,
                deny=(settings.DISALLOWED_DOMAINS[0]),
                unique=('Yes')
            ),
            callback='parse_my_url',
            follow=True
        ),
        # crawl external links but don't follow them
        Rule(
            LinkExtractor(
                allow=(''),
                deny=(settings.DISALLOWED_DOMAINS[0]),
                unique=('Yes')
            ),
            callback='parse_my_url',
            follow=False
        )
    ]

    def parse_my_url(self, response):
        if response.status in report_if:
            item = MyItems()
            item['referer'] = response.request.headers.get('Referer', None)
            item['status'] = response.status
            item['response']= response.url
            yield item
        yield None
