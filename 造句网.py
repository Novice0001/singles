# -*- coding:utf-8 -*-
# author lan

import requests
import json
import time
from lxml.html import etree
from pymongo import MongoClient
from selenium import webdriver

# 连接到MongoDB
con = MongoClient("127.0.0.1", 27017)
db = con.zaoju
my_set = db.zuoju1

url_1 = "http://zaojv.com"
for page in range(1, 858):
    url = "http://zaojv.com/word_"+str(page)+".html"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d3da4e9d1850926fa70a5f7d1c5e54b981523079579; Hm_lvt_5269e069c39f6be04160a58a5db48db4=1523079580; UM_distinctid=1629e9e0c8a187-053bc72d38b15f-4446062d-15f900-1629e9e0c8d4f1; CNZZDATA5176529=cnzz_eid%3D740175209-1523075425-%26ntime%3D1523075425; _ga=GA1.2.938684512.1523079582; _gid=GA1.2.2048579633.1523079582; Hm_lpvt_5269e069c39f6be04160a58a5db48db4=1523079766",
        "Host": "zaojv.com",
        "Referer": "http://zaojv.com/word_2.html",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    list_url = html.xpath("//ul[@class='c1 ico2']/li[@class='dotline']/a/@href")
    for url_2 in list_url:
        print(url_1+url_2)
        response_1 = requests.get(url=url_1+url_2, headers=headers)
        html_1 = etree.HTML(response_1.text)
        title = html_1.xpath("//h2/text()")[0]
        content = html_1.xpath("//div[@class='viewbox']/div[@id='content']/div[@id='all']/div/text()")[0:10]
        print(title)
        print(content)
        my_set.insert({"title": title, "content": content})








