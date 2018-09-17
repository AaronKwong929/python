import re
import requests
# from lxml import etree


headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def get_vedio_info(url):
    html = requests.get(url, headers=headers)
    # selector = etree.HTML(html.text)
    # name = selector.xpath('//*[@id="submit-video-list"]/ul[2]/li[1]/a[2]/text()')
    name = re.findall('<a href=".*?"target="_blank" title="(.*?)" class="title">', html.text, re.S)
    '''reg = r' target="_blank" title="[.*\S]*" class="title">'
    namere = re.compile(reg)
    nameList = re.findall(namere, html)'''
    # clicks = selecto.xpath('//*[@id="submit-video-list"]/ul[2]/li[1]/div/span[1]/text()')[0]
    # time = selector.xpath('//*[@id="submit-video-list"]/ul[2]/li[1]/div/span[2]/text()')[0]
    # print('视频名称:' + name + '   播放量：' + clicks + '   发布时间：' + time)
    print(name)


if __name__ == '__main__':
    url = 'https://space.bilibili.com/122879/#/video'
    get_vedio_info(url)