from lxml import etree
import requests
import csv
f = open('C://Users/Arron/Desktop/doubantop250.csv', 'wt')#, newline='', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(('name','url'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 50, 25)]

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        writer.writerow((name))
f.close()