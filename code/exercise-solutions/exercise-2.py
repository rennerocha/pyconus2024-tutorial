import scrapy


class QuotesScrollSpider(scrapy.Spider):
    name = "quotes_scroll"
    allowed_domains = ["quotes.toscrape.com"]
    api_url = "https://quotes.toscrape.com/api/quotes?page={page}"

    def start_requests(self):
        yield scrapy.Request(self.api_url.format(page=1))

    def parse(self, response):
        data = response.json()

        for quote in data.get("quotes"):
            yield {
                "quote": quote.get("text"),
                "author": quote.get("author").get("name"),
                "author_url": response.urljoin(
                    quote.get("author").get("goodreads_link")
                ),
                "tags": quote.get("tags"),
            }

        current_page = data.get("page")

        if data.get("has_next"):
            next_page = current_page + 1
            yield scrapy.Request(
                self.api_url.format(page=next_page),
            )
