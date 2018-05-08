import requests


url = "https://www.jianyu360.com/jylab/supsearch/index.html"

headers = {
    "Host": "www.jianyu360.com",
    "Origin": "https://www.jianyu360.com",
    "Referer": "https://www.jianyu360.com/jylab/supsearch/index.html",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}

data = {
    "keywords": "思科",
    "selectType": "title",
}

response = requests.post(url=url, headers=headers)
print(response.text)

