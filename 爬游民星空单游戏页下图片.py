import requests
from lxml import etree
import urllib.request

src_links = []
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'https://down.gamersky.com/pc/201411/486874.shtml'

html = requests.get(url, headers=headers)
selector = etree.HTML(html.text)

infos = selector.xpath('///div[5]/ul/li/img/@src')

for info in infos:
    src_links.append(info)

# 文件写入
count = 1
for src_link in src_links:
    f = open("C:/Users/Arron/Desktop/photo/" + str(count) + ".jpg", 'wb')
    f.write((urllib.request.urlopen(src_link)).read())
    f.close()
    print('第' + str(count) + '张图片已爬取。')
    count += 1
