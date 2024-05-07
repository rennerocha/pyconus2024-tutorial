import scrapy


class PyConUS2024Spider(scrapy.Spider):
    name = "pyconus"

    start_urls = [
        "https://us.pycon.org/2024/schedule/tutorials/",
    ]

    def parse(self, response):
        for tutorial in response.css(".presentation"):
            yield {
                "speaker": tutorial.css(".speaker::text").get().strip(),
                "url": response.urljoin(tutorial.css(".title a::attr(href)").get()),
                "title": tutorial.css(".title a::text").get(),
            }
