# -*- coding: utf-8 -*-
import scrapy


class LovequotesSpider(scrapy.Spider):
    name = 'lovequotes'
    allowed_domains = ['brainyquote.com']
    start_urls = ['https://www.brainyquote.com/quotes/topics/topic_love.html']

    def parse(self, response):
        self.log("Visit Successful\n" + response.url)
        for quote in response.css('div.bqcpx'):
            item = {
                'quote_text': quote.css('a.b-qt::text').extract_first(),
                'tags': quote.css('a.bq-aut::text').extract_first()
            }
            yield item
