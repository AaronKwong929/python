# 重新写个静态网页的爬虫练练手
import requests
from lxml import etree
import time
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
url = 'http://www.qq.com/'

html = requests.get(url, headers=headers)
selector = etree.HTML(html.text)
infos = selector.xpath('//*[@id="newsInfoQuanguo"]')
for info in infos:
    names = info.xpath('div/div/ul/li/a/text()')
    for name in names:
        print(name)
        time.sleep(1)