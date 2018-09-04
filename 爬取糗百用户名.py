import requests
from lxml import etree
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
url = 'http://qiushibaike.com/text/'
res = requests.get(url, headers=headers)
selector = etree.HTML(res.text)
id = selector.xpath('//*[@id="qiushi_tag_118732380"]/div[1]/a[2]/h2/text()')
print(id)

# failed
