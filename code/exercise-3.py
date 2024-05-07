import json
import scrapy


class QuotesJSSpider(scrapy.Spider):
    name = "quotes_js"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]

    def parse(self, response):
        raw_quotes = response.xpath("//script").re_first(r"var data = ((?s:\[.*?\]));")
        quotes = json.loads(raw_quotes)
        for quote in quotes:
            yield {
                "quote": quote.get("text"),
                "author": quote.get("author").get("name"),
                "author_url": response.urljoin(
                    quote.get("author").get("goodreads_link")
                ),
                "tags": quote.get("tags"),
            }
        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )
