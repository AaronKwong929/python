import requests
from lxml import etree
import re
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
musictop = mydb['musictop']

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def get_url_music(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//a[@class="nbg"]/@href')
    for music_href in music_hrefs:
        get_music_info(music_href)


def get_music_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    # name = re.findall('<div id="wrapper"><h1><span>(.*?)</span>', html.text, re.S)[0]  # （待解决）正则表达式爬取专辑名失败
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    author = selector.xpath('//*[@id="info"]/span/span/a/text()')[0]  # （成功）xpath爬取作者
    # author = re.findall('表演者:.*?>(.*?)</a>', html.text, re.S)[0]  # （成功）正则表达式爬取作者  # copy outer html观察网页结构写出正则表达式的非贪心算法
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />', html.text, re.S)  # 流派要用正则表达式爬取，xpath爬出其他垃圾信息
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()
    publishTime = re.findall('发行时间:</span>&nbsp;(.*?)<br />', html.text, re.S)[0].strip()
    publishers = re.findall('出版者:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(publishers) == 0:
        publisher = '未知'
    else:
        publisher = publishers[0].strip()
    # score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]  #xpath爬出垃圾信息
    score = re.findall(
        '<strong class="ll rating_num" property="v:average">(.*?)</strong>', html.text, re.S)[0].strip()
    # print("专辑：" + name, "作者：" + author, "流派：" + style, "发行时间：" + publishTime, "出版商：" + publisher, "评分：" + score)
    info = {
        'name': name,
        'author': author,
        'style': style,
        'publishTime': publishTime,
        'publisher': publisher,
        'score': score
    }
    musictop.insert_one(info)


if __name__ == '__main__':
    urls = [
        'https://music.douban.com/top250?start={}'.format(str(i))
        for i in range(0, 25, 25)
    ]
    for url in urls:
        get_url_music(url)
