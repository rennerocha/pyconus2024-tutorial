import scrapy


class QuotesPlaywrightSpider(scrapy.Spider):
    name = "quotes-playwright"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,
        },
    }

    def start_requests(self):
        yield scrapy.Request(
            url="http://quotes.toscrape.com/js/",
            meta={
                "playwright": True,
            },
        )

    async def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            yield {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "author_url": response.urljoin(quote.css("span a::attr(href)").get()),
                "tags": quote.css(".tag *::text").getall(),
            }

        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get()),
            meta={
                "playwright": True,
            },
        )
