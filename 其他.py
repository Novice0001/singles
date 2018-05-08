# -*- coding:utf-8 -*-
# author lan
import requests
import json

ip = requests.get('http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=3ddb40106f2d4f3f8a44c112b6bb32d6&count=1&expiryDate=0&format=1').text
# ip = requests.get('http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=3ddb40106f2d4f3f8a44c112b6bb32d6&count=1&expiryDate=0&format=2').text
port = json.loads(ip)['msg'][0]['port']
ip = json.loads(ip)['msg'][0]['ip']
print(ip, port)
proxy = {'http':ip+':'+port}
print(proxy)
with open("代理ip.txt", "a+", encoding="utf-8") as f:
    f.write(str(proxy)+'\n')

