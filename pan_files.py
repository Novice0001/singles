# -*- coding:utf-8 -*-
# author lan

import requests
import re
from lxml.html import etree

headers = {
    # "Cookie": " __utma=212754963.396868507.1522396183.1522396183.1522396183.1; __utmc=212754963; __utmz=212754963.1522396183.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PageState=%7B%22dictionary%22%3A%22uk%22%2C%22lookup%22%3Anull%2C%22advboxopen%22%3Afalse%2C%22hideOffensiveWords%22%3Afalse%2C%22showMore%22%3Afalse%2C%22c%22%3A%7B%7D%2C%22pageSize%22%3A40%2C%22showLevel%22%3A%22a1_c2%22%7D; __utmt=1; __utmb=212754963.27.10.1522396183",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Authorization": "Basic ZW5nbGlzaHByb2ZpbGU6dm9jYWJ1bGFyeQ==",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "__utmz=212754963.1522396183.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=212754963; PageState=%7B%22dictionary%22%3A%22uk%22%2C%22lookup%22%3Anull%2C%22advboxopen%22%3Afalse%2C%22hideOffensiveWords%22%3Afalse%2C%22showMore%22%3Afalse%2C%22c%22%3A%7B%7D%2C%22pageSize%22%3A40%2C%22showLevel%22%3A%22a1_c2%22%7D; __utma=212754963.396868507.1522396183.1522581728.1522585813.7",
    "Host": "vocabulary.englishprofile.org",
    "Referer": "http://vocabulary.englishprofile.org/dictionary/word-list/uk/a1_c2/K/2001716",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",

   }
# 第一层的url拼接


# 详情页小实验
from scrapy.selector import Selector
import csv
import multiprocessing
import time
import random
class spider:
    # def __init__(self):
        # self.head = self.writer.writerow(["HEADOFWORD", "WORD", "POS"])
    # 'A ', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    def sp(self):
        list_1 = ['M', 'Q']  # 'L', 'M', 'N', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        for i in list_1:
            HEADOFWORD = i
            url = "http://vocabulary.englishprofile.org/dictionary/word-list/uk/a1_c2/" + i
            url_1 = "http://vocabulary.englishprofile.org"
            # url = "http://vocabulary.englishprofile.org/dictionary/word-list/uk/a1_c2/C"
            response = requests.get(url=url, headers=headers)
            # print(response.text)
            # 获取第二层的url
            html = etree.HTML(response.text)
            href_1 = html.xpath("//*[@id='groupResult']/ul/li/a/@href")
            # print(href_1)
            for url_2 in href_1:
                url_3 = url_1 + url_2
                # print(url_3)
                response_1 = requests.get(url=url_3, headers=headers)
                html_2 = etree.HTML(response_1.text)
                # 获取第三层的url
                href_2 = html_2.xpath("//*[@id='result']/ul/li/a/@href")
                for i in href_2:
                    url_3 = url_1 + i
                    print(url_3)
                    response = requests.get(url=url_3, headers=headers)
                    html = response.text
                    # print(html)
                    se = Selector(text=html)
                    items = se.xpath("//div[@class='gwblock']")
                    WORD = se.xpath(".//h1[@class='hw']/text()").extract_first(default=None)
                    POS = se.xpath(".//b[@class='pos']/text()").extract_first(default=None)
                    print("WORD=", WORD)
                    print("POS=", POS)
                    for item in items:
                        MEANING = item.xpath(".//h3[@class='gw']/text()").extract_first(default=None)
                        LEVEL = item.xpath(".//span[contains(@class,'freq')]/text()").extract_first()
                        DEFINITION = item.xpath(".//span[@class='def']/text()").extract_first()
                        DICTIONARYEXAMPLE = ''.join(item.xpath(".//div[contains(@class,'examp')]/blockquote/text()").extract())
                        LEARNEREXAMPLE = item.xpath('.//div[@class="sense"]/blockquote/text()').extract_first()
                        print("MEANING=", MEANING)
                        print("LEVEL=", LEVEL)
                        print("DEFINITION=", DEFINITION)
                        print("DICTIONARYEXAMPLE=", DICTIONARYEXAMPLE)
                        print("LEARNEREXAMPLE=", LEARNEREXAMPLE)
                        with open("test.csv", "a+", newline='') as csvfile:
                            self.writer = csv.writer(csvfile)
                            try:
                                self.writer.writerow('{},{},{},{},{},{},{},{}'.format(HEADOFWORD, WORD, POS, MEANING, LEVEL, DEFINITION, DICTIONARYEXAMPLE, LEARNEREXAMPLE).split(','))
                                print('{},{},{},{},{},{},{},{}'.format(HEADOFWORD, WORD, POS, MEANING, LEVEL, DEFINITION, DICTIONARYEXAMPLE, LEARNEREXAMPLE).split(','))
                            except:
                                break

s = spider()
s.sp()



