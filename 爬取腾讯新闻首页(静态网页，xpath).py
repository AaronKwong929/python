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
# 以下是将大标签一直写到a标签之前，每一个新闻标题作为一个单独的列表存在，用[0]来输出新闻标题
infos = selector.xpath('//*[@id="newsInfoQuanguo"]/div/div/ul/li')
for info in infos:
    name = info.xpath('a/text()')[0]
    print(name)
    time.sleep(1)
  # 以下是将所有新闻标题放在一个列表内，不用[0]来控制列表,再做一个for循环输出，时间复杂度高一点    
'''
infos = selector.xpath('//*[@id="newsInfoQuanguo"]')
for info in infos:
    names = info.xpath('div/div/ul/li/a/text()')
    for name in names:
        print(name)
'''
    