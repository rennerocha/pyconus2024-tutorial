import json
import scrapy


class QuotesJSSpider(scrapy.Spider):
    name = "quotes_js"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]

    def parse(self, response):
        # 1. Find the raw data inside the HTML
        raw_quotes = response.xpath("//script").re_first(r"var data = ((?s:\[.*?\]));")

        # 2. With the raw data, convert it to Python and parse it

        # 3. Don't forget we have pagination here too