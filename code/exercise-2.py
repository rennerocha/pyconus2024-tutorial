import scrapy


class QuotesScrollSpider(scrapy.Spider):
    name = "quotes_scroll"
    allowed_domains = ["quotes.toscrape.com"]

    def start_requests(self):
        # What would be a good first request for this spider?
        ...

    def parse(self, response):
        # API response is a JSON content
        data = response.json()

        # Parse the data here