import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # 1. Get the list of quotes availabe at the page

        # 2. Parse each quote found and yield the quote item

        # 3. Follow the next page link
        ...