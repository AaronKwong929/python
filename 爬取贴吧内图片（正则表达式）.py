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
    reg = r'src="([.*\S]*\.jpg)" size='  # 正则内容对应每个贴吧的内容都不一样，需要对图片检查找jpeg后面的东西
    imgre = re.compile(reg)
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