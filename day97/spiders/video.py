# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector
from ..items import Day97Item
from scrapy.http.cookies import CookieJar
import json
class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['my.tokyo-hot.com']
    start_urls = ['https://my.tokyo-hot.com/product/']
    cookie_dict=None

    def parse(self, response):
        cookie_obj = CookieJar()
        cookie_obj.extract_cookies(response, response.request)
        self.cookie_dict = cookie_obj._cookies
        obj=Selector(response=response).xpath('//div[@id="main"]//li[@class="detail"]')
        c=0

        for item in obj:
            href=item.xpath('./a[@href]/img/@src').extract()[0]
            url=item.xpath('./a[@href]/@href').extract()[0]
            url1=str("https://my.tokyo-hot.com"+str(url))

            title=str(item.xpath('./a[@class="rm"]/img/@title').extract()[0])

            print(title)
            c += 1
            print(c)

            t=title+'.jpg'
            t1=t+'\n'
            h=url1
            with open("list_all.jason","a") as f1:
                f1.write(t1)                        #check
            dict={}
            dict[t]=h
            with open("list_all_href.jason","a") as f2:
                f2.write(json.dumps(dict))
                f2.write("\n")

            yield Request(url=url1,
                          meta={'title': title},
                          callback=self.inner,dont_filter = True
                          )

        page=Selector(response=response).xpath('//div[@id="main"]//div[contains(@class,"navi")]/ul/li[@class="next"]/a/@href').extract()[0]
        print("当前页码:",page)
        page_url='https://my.tokyo-hot.com/product/'+page
        # print(page_url)
        yield Request(url=page_url)



    def inner(self,response):
        title= response.meta['title']
        obj = Selector(response=response).xpath('//div[@id="container"]/div[contains(@class,"movie")]/div[@class="in"]/div[contains(@class,"flowplayer")]/video[@poster]/@poster').extract()[0]
        if not obj:
            obj = Selector(response=response).xpath(
                '//div[@id="container"]/div[contains(@class,"movie")]/div[@class="in"]/div[contains(@class,"flowplayer")]/dl8-video[@poster]/@poster').extract()[
                0]

        # print(c)
        itemObj = Day97Item(title=title, href=obj)  # 封装，给pipeline处理
        yield itemObj
