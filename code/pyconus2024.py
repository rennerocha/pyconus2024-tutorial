import scrapy


class PyConUS2024Spider(scrapy.Spider):
    name = "pyconus"

    start_urls = [
        "https://us.pycon.org/2024/schedule/tutorials/",
    ]

    def parse(self, response):
        for tutorial in response.css(".calendar a::text").getall():
            yield {"title": tutorial}
