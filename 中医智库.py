import requests
import json
import base64, sys
import pyaes.aes
import zlib
from lxml.html import etree
from queue import Queue
from threading import Thread

class project():
    def __init__(self):
        self.url = "https://www.zk120.com"

    def index(self):
        url_1 = self.url+"/ji/group/?nav=ahz"
        headers = {
            "referer": "https://www.zk120.com/ji/?nav=ahz",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        response = requests.get(url=url_1, headers=headers, proxies="{'http': '110.89.121.60:41834'}")
        html = etree.HTML(response.text)
        return html

    def parse(self, html):
        src = html.xpath("//section[@class='ice_bg space_pr space_pl'][2]/ul[@class='group_list clearfix']/li/a/@href")
        for url2 in src:
            url3 = self.url+url2
            response_1 = requests.get(url=url3)
            html_1 = etree.HTML(response_1.text)
            name = html_1.xpath("//li[@class='book_wrapper space_pr']/div[@class='book_info pr']/h3/text()")
            name_url = html_1.xpath("//li[@class='book_wrapper space_pr']/div[@class='book_info pr']/p[@class='group_btns']/a/@href")
            # print(name, name_url)
            for i in zip(name, name_url):
                name_url1 = self.url+i[1].replace("read", "content")
                response_2 = requests.get(url=name_url1)
                # print(response_2.text)
                url_json = json.loads(response_2.text)
                data = url_json["data"]
                return data

    def main(self, data):
                missing_padding = 4 - len(data) % 4
                print(missing_padding)
                if missing_padding:
                    data += '=' * missing_padding
                # 将分开的内容进行解码
                # print(text)
                content = base64.b64decode(data.encode('utf-8'))
                # print(content)
                aes = pyaes.AESModeOfOperationCFB(key=b"61581af471b166682a37efe6", iv=b"c8f203fca312aaab",
                                                  segment_size=16)
                aes_text = aes.decrypt(content)
                # 解压缩
                text_zip = json.loads(zlib.decompress(aes_text))
                # 输出结果
                text_code = text_zip.get("text").encode("utf-8", "ignore")
                print(str(text_code, encoding='utf-8'))


pro = project()
html = pro.index()
data = pro.parse(html)
print(data)
pro.main(data)






# class page_index(Thread):
#     def __init__(self):
#         super(page_index, self).__init__()
#         self.url = "https://www.zk120.com/ji/group/?nav=ahz"
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
#                           "(KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
#         }
#     def run(self):
#         response = requests.get(url=self.url, headers=self.headers)
#         html = etree.HTML(response.text)
#         pageQueue.put(html)
#
# class page_parse(Thread):
#
#     def run(self):
#         while True:
#             if pageQueue.empty():
#                 break
#             response = pageQueue.get()
#             self.parse_xpath(response)
#
#     def parse_xpath(self, response):
#         srcs = response.xpath("//ul[@class='group_list clearfix']/li/a[@class='ellipsis']/@href")
#         print(srcs)
#
# pageQueue = Queue()
# def main():
#     # --------获取url线程--------
#     page_index_list = []
#     for i in range(1, 6):
#         pag = page_index()
#         pag.start()
#         page_index_list.append(pag)
#     for page in page_index_list:
#         page.join()
# # ---------解析线程------------
#     page_parse_list = []
#     for i in range(1, 6):
#         parse = page_parse()
#         parse.start()
#         page_parse_list.append(parse)
#         for par in page_parse_list:
#             par.join()

    















