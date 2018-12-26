# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class Day97Pipeline(object):

    def process_item(self, item, spider):
        # c=item['title']
        # if item['title'] in c:
        #     c.remove(item['title'])
        # print(c)
        name = str(item['title']) + '.jpg'
        url = item['href']
        # href_url = url if url.startswith('http') else 'http://www.xiaohuar.com%s' % url

        print(name)
        file='img/'+name
        response = requests.get(url)
        with open(file, "wb") as f:
            f.write(response.content)
        name_li=name+'\n'

        with open('list.jason','a') as b:
            b.write(name_li)  #for check
        return item
