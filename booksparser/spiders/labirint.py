import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem

class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/2540/"]

    def parse(self, response: HtmlResponse):

        next_page = response.xpath("//a[@title='Следующая (Ctrl ->)']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//div[@data-title='Все в жанре «Мистическая зарубежная фантастика»']//a[@class='product-title-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_book_page)


    def parse_book_page(self, response: HtmlResponse):
        title = response.xpath("//h1/text()").get()
        author = response.xpath("//a[@data-event-label='author']/text()").get()
        translator = response.xpath("//a[@data-event-label='translator']/text()").get()
        url = response.url
        general_price = response.xpath("//span[@class='buying-priceold-val-number']/text()").get()
        your_price = response.xpath("//span[@class='buying-pricenew-val-number']/text()").get()
        currency = response.xpath("//span[@class='buying-pricenew-val-currency']/text()").get()
        return BooksparserItem(title=title, author=author, translator=translator, url=url, general_price=general_price, your_price=your_price, currency=currency)

