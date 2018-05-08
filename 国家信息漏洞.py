# -*- coding:utf-8 -*-
# author lan

import requests
from lxml.html import etree
import pymysql

con = pymysql.connect("127.0.0.1", "root", "123456", database="1511b", port=3306, charset="utf8")
cursor = con.cursor()
cursor.execute("drop table if EXISTS loutong")
cursor.execute("create table loutong(id INT PRIMARY KEY auto_increment, CNNVD VARCHAR(100), CVE VARCHAR(100), 厂商 VARCHAR(100))")
url_2 = "http://www.cnnvd.org.cn"

# url = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag"
for page in range(1, 200):
    url = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno="+str(page)+"&repairLd="

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "SESSION=deb7b51b-83f3-4d9c-9fb2-91c9929eccf9; topcookie=a1",
        "Host": "www.cnnvd.org.cn",
        "Referer": "http://www.cnnvd.org.cn/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    src = html.xpath("//ul/li/div/a/@href")
    for i in src:
        response_1 = requests.get(url=url_2+i, headers=headers)
        html_1 = etree.HTML(response_1.text)
        CNNVD = html_1.xpath("//div[@class='detail_xq w770']/ul/li[1]/span/text()")
        CVE_1 = html_1.xpath("//div[@class='detail_xq w770']/ul/li[3]/a/text()")
        CVE_2 = html_1.xpath("//div[@class='detail_xq w770']/ul/li[3]/span/text()")
        content_1 = html_1.xpath("//div[@class='detail_xq w770']/ul/li[8]/span/text()")
        content_2 = html_1.xpath("//div[@class='detail_xq w770']/ul/li[8]/a/text()")
        CVE = CVE_1[0]
        CNNVD_3 = CNNVD[0]
        print(CNNVD_3)
        print(CVE)
        if content_2 == []:
            content_2 = None
            print(content_2)
            cursor.execute("insert into loutong(CNNVD,CVE, 厂商) VALUES ('%s',' %s','%s');" % (CNNVD_3, CVE, content_2))
            con.commit()
    CNNVD_3 = CNNVD[0]
    CVE = CVE_1[0]
    content = "".join(content_2+content_1), " \xa0"
    CVE_3 = CVE[0]
    content_3 = content[0]
    print(CVE_3)
    print(content_3)
    cursor.execute("insert into loutong(CNNVD,CVE, 厂商) VALUES ('%s',' %s','%s');" % (CNNVD_3, ' ', ''))
    con.close()












