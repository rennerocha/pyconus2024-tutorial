import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            yield {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "author_url": response.urljoin(quote.css("span a::attr(href)").get()),
                "tags": quote.css(".tag *::text").getall(),
            }

        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )
