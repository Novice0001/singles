
import requests
from lxml.html import etree
import matplotlib.pyplot as plt

class project():
    def __init__(self):
        pass

    def index_1(self):
        # http://newhouse.sh.fang.com/house/s/?ctm=1.gz.xf_search.head.4
        url = "http://newhouse.sh.fang.com/house/s/?ctm=1.gz.xf_search.head.2"
        self.headers = {
            "Referer": "http: // sh.fang.com /",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        response = requests.get(url=url, headers=self.headers)
        response.encoding = response.apparent_encoding
        html = etree.HTML(response.text)
        title = html.xpath("//a/span[@class='sngrey']/text()")
        url_1 = html.xpath("//div/ul/li/div/div/a/@href")
        return url_1

    def index_2(self, url_1):  # 二级页面
        content_list = []
        dynamic_list = []
        Huxing_list = []
        for ur in url_1:
            response_2 = requests.get(url=ur, headers=self.headers)
            html = etree.HTML(response_2.text)
            # 楼房详情URL
            content_url = html.xpath("//div/div/div[@id='orginalNaviBox']/a/@href")[1]
            # 楼房动态URL
            dynamic_url = html.xpath("//div/div/div[@id='orginalNaviBox']/a/@href")[2]
            # 楼房详情URL
            Huxing_url = html.xpath("//div/div/div[@id='orginalNaviBox']/a/@href")[3]
            content_list.append(content_url)
            dynamic_list.append(dynamic_url)
            Huxing_list.append(Huxing_url)
        tuple_1 = (content_list, dynamic_list, Huxing_list)
        return tuple_1

    def index_3(self, tuple_1):
        for i in tuple_1[0]:
            response = requests.get(url=i, headers=self.headers)
            response.encoding = response.apparent_encoding
            html = etree.HTML(response.text)


pro = project()
pro_1 = pro.index_1()
pro_2 = pro.index_2(pro_1)
pro_3 = pro.index_3(pro_2)

