import scrapy


class PyConUS2024Spider(scrapy.Spider):
    name = "pyconus"

    start_urls = [
        "https://us.pycon.org/2024/schedule/tutorials/",
    ]

    def parse(self, response):
        for tutorial in response.xpath('//div[@class="presentation"]'):
            yield {
                "speaker": tutorial.xpath('./div[@class="speaker"]/text()')
                .get()
                .strip(),
                "url": response.urljoin(tutorial.xpath(".//a/@href").get()),
                "title": tutorial.xpath(".//a/text()").get(),
            }
