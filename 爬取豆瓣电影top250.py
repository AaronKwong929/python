import requests
from lxml import etree
import re

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def get_url_movie(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    movie_hrefs = selector.xpath('//div[@class="hd"]/a/@href')
    for movie_href in movie_hrefs:
        get_movie_info(movie_href)


def get_movie_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]  # 抓大标签
        actor = actors.xpath('string()')  # 参考https://blog.csdn.net/jiangchao858/article/details/63314426 text()和string()的区别
        #                                   写成actors.xpath('string(.)')为返回当前节点的所有文本内容并拼接成字符串
        style = re.findall('<span property="v:genre">(.*?)</span>', html.text, re.S)  # 括号后添加[0]只能返回第一个类型，re.findall()返回一个列表，在下方进行输出时使用" ".join(style)可以把列表合并成一个字符串输出
        '''style1 = selector.xpath('//*[@id="info"]/span[5]/text()')[0]  # 不能用xpath，有一些电影只有两个类型，有一些有4个，只有2个的在span[7]就会爬取出下一项国家地区
        style2 = ' ' + selector.xpath('//*[@id="info"]/span[6]/text()')[0]
        style = style1 + style2'''
        country = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>', html.text, re.S)[0]
        language = re.findall('<span class="pl">语言:</span>(.*?)<br/>', html.text, re.S)[0]
        release_time = re.findall('<span property="v:initialReleaseDate" content=".*?">(.*?)</span>', html.text, re.S)
        movie_time = re.findall('<span property="v:runtime" content=".*?">(.*?)</span>', html.text, re.S)
        score = re.findall('<strong class="ll rating_num" property="v:average">(.*?)</strong>', html.text, re.S)[0]
        print('电影名：' + name + '   导演：' + director + '   演员：' + actor + '   类型：' + " ".join(style) + '   制片国家/地区：' + country + '   语言：' + language + '   上映时间：' + " ".join(release_time) + '   片长：' + " ".join(movie_time) + '   评分：' + score)
        print()
        # t列表合并函数中 "".join() 双引号中的内容为字符串中的分隔条件，此处空格即为将列表每一个内容空格隔开  # 参考https://blog.csdn.net/roytao2/article/details/53433373
        # print(" ".join(style))
    except IndexError:
        print("error")
        pass


if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start={}'.format(str(i))for i in range(0, 250, 25)]
    for url in urls:
        get_url_movie(url)