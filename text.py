import requests
from lxml import etree

src_links = []
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = 'https://down.gamersky.com/pc/201411/486874.shtml'

html = requests.get(url, headers=headers)
html.encoding = "utf-8"  # 乱码解决核心
selector = etree.HTML(html.text)
name = selector.xpath('//div[@class="tit"]/text()')[0]
print(name)
