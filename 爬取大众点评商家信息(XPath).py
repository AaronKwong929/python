import requests
from lxml import etree
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = 'https://www.dianping.com/search/keyword/4/0_北京路/p1'
html = requests.get(url, headers=headers)
selector = etree.HTML(html.text)
names = selector.xpath('//div[@class="txt"]/div[@class="tit"]/a/h4/text()')
comments = selector.xpath(
    '//div[@class="txt"]/div[@class="comment"]/a[1]/b/text()')
averages = selector.xpath(
    '//div[@class="txt"]/div[@class="comment"]/a[2]/b/text()')
styles = selector.xpath(
    '//div[@class="txt"]/div[@class="tag-addr"]/a[1]/span/text()')
add1s = selector.xpath(
    '//div[@class="txt"]/div[@class="tag-addr"]/a[2]/span/text()')
add2s = selector.xpath(
    '//div[@class="txt"]/div[@class="tag-addr"]/span/text()')
print(names)