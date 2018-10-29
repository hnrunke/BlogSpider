# -*- coding: utf-8 -*-
import scrapy, re
from scrapy import Request
from scrapy.selector import Selector
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from urllib.parse import quote
from BlogSpider.items import SpiderResult


class FaceBookSpider(scrapy.Spider):
    name = 'facebook_search'
    allowed_domains = ['mobile.facebook.com']

    def __init__(self, **kwargs):
        kwargs.pop('_job')
        q = quote(kwargs.get('q'), 'trump')
        # q = 'Obama'
        # Refer = kwargs.get('Refer')
        self.uuid = kwargs.get('uuid', 1000)
        super(FaceBookSpider, self).__init__(**kwargs)
        self.start_urls = [
            f'https://mobile.facebook.com/graphsearch/str/{q}/stories-keyword/stories-public'
        ]

        self.cookie = {
            "c_user": "100029290456102",
            "datr": "-H_WW_vvhU8IH2ubTbyYADMb",
            "fr": "16W3TC9aYo8AFQlDY.AWUzW6MsyDuCY3-wHZJqvksijWY.Bb1n_4.X_.AAA.0.0.Bb1oAN.AWUJwWkZ",
            "noscript": "1",
            "pl": "n",
            "sb": "-H_WWyXh0g9_SuVepBzYCl9Z",
            "xs": "31%3AV_DdtJ8izYpRfw%3A2%3A1540784141%3A-1%3A-1",
        }

    def start_requests(self):
        requestList = []
        for url in self.start_urls:
            meta = {'page': '1'}
            requestList.append(scrapy.Request(url=url, cookies=self.cookie, meta=meta))
        return requestList

    def parse(self, response):
        spiderResult = SpiderResult()
        spiderResult['uuid'] = self.uuid
        spiderResult['result'] = response.body
        pageNumber = response.meta['page']
        if not pageNumber:
            pageNumber = 1
        spiderResult['page'] = pageNumber
        yield spiderResult

        sel = Selector(response)
        pages = sel.xpath('//div[@id="see_more_pager"]/a/@href').extract()
        if len(pages) > 0:
            for page in pages:
                meta = {'page': str(int(pageNumber) + 1)}
                yield scrapy.Request(url=page, cookies=self.cookie, meta=meta)
