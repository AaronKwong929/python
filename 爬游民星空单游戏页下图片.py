import requests
from lxml import etree
import urllib.request

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

src_links = []

urls = [
    'https://down.gamersky.com/pc/201411/486874.shtml',
    'https://down.gamersky.com/pc/201604/739324.shtml'
]


for url in urls:
    count = 1
    shortName = url.split('https://down.gamersky.com/pc/')[1]
    html = requests.get(url, headers=headers)
    html.encoding = "utf-8"  # 乱码解决核心
    selector = etree.HTML(html.text)
    infos = selector.xpath('//div[5]/ul/li/img/@src')
    name = selector.xpath('//div[@class="tit"]/text()')[0]
    for info in infos:
        src_links.append(info)
    for src_link in src_links:
        f = open("C:/Users/Arron/Desktop/photo/" + name + str(count) + ".jpg", 'wb')
        f.write((urllib.request.urlopen(src_link)).read())
        f.close()
        print(name + '第' + str(count) + '张图片已爬取。')
        count += 1
    src_links = []
    count = 0
