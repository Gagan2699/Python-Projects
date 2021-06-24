import scrapy

from daily_wiki.items import Article

class ArticleSpider(scrapy.Spider):
    name='aticle'
    allowed_domains=['en.wikipedia.org']
    start_urls=['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    custom_settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'file:///tmp/featured-articles.json'
    }
    def parse(self,respsonse):
        host=self.allowed_domains[0]
        for link in response.css("featured_article_metadata > a"):
            yield Article(
                title=link.attrib.get("title"),
                link= f"https://{host}{link.attrib.get(href')}"
            )
