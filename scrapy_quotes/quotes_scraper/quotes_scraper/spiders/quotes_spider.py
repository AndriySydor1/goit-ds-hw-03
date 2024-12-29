import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "tags": quote.css("div.tags a.tag::text").getall(),
                "author": quote.css("span small.author::text").get(),
                "quote": quote.css("span.text::text").get()
            }
        
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
            