import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


htmls = [
    'https://tieba.baidu.com/p/5458607665?pn={}'.format(str(i))
    for i in range(1, 3)
]


def get_pic(html):
    reg = r'height="\d*" src="([.*\S]*\.jpg)"'
    # reg = r'src="([.*\S]*\.jpg)"'  # 爬到一半失败了，原因未知，还是根据outerHTML构造正则表达式，更加精确定位
    imgre = re.compile(reg)
    imgList = re.findall(imgre, html)
    return imgList


try:
    imgName = 0
    for html in htmls:
        url = getHtml(html)
        url = url.decode('utf-8')
        imgList = get_pic(url)
        for imgPath in imgList:
            f = open("C:/Users/Arron/Desktop/photo/" + str(imgName) + ".jpg",
                     'wb')
            f.write((urllib.request.urlopen(imgPath)).read())
            f.close()
            imgName += 1
except IOError:
    print("Error.")
