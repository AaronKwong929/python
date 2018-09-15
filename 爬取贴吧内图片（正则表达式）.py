import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


html = getHtml("http://tieba.baidu.com/p/5439602441")
html = html.decode('UTF-8')


def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    # reg = r'src="([.*\S]*\.jpg)" size='  # 正则内容对应每个贴吧的内容都不一样，需要对图片检查找jpeg后面的东西
    reg = r'src="([.*\S]*\.jpg)" size='  # []←为字符集，"."为匹配任意字符，"*"为匹配0次到无限次,"\S"为匹配非空白字符,()括号为返回内容
    # 整个字符集再匹配0到无限次，复制outer html观察可知：
    # src="https://imgsa.baidu.com/forum/w%3D580/sign=4c9a9f3955df8db1bc2e7c6c3921dddb/abf17d1ed21b0ef40b2f06ffd6c451da80cb3e7a.jpg" size=
    # 写出 r'src="([.*\S]*\.jpg)" size='
    # 关于正则表达式的使用：
    # https://blog.csdn.net/vonsdite/article/details/76572999
    imgre = re.compile(reg)  # re.compile(reg[,flag]),详见下链接
    imglist = re.findall(imgre, html)
    return imglist


imgList = getImg(html)
imgName = 0
for imgPath in imgList:
    f = open("C:/Users/Arron/Desktop/photo/" + str(imgName)+".jpg", 'wb')
    f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    imgName += 1


print("爬取完成")