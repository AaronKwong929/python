from lxml import etree
import requests
import csv
f = open('C://Users/Arron/Desktop/doubantop250.csv', 'wt', newline='', encoding='utf-8')  #  a不写utf-8会无法编译
writer = csv.writer(f)
writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')  # 这一个还是不懂怎么写出来
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]  # name和url要自己找
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]  # 复制xpath看循环以外的编码
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]  # 网页构造，从后往前读更加准确些，从前往后发现bug
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]  # 此处不写span[2]就会把书本的原名爬取到 原因未明
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else "无"
        writer.writerow((name, url, author, publisher, date, price, rate, comment))
f.close()