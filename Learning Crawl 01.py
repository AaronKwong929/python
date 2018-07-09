'''
# 示例1 输出某网址的全部HTML代码
from urllib.request import urlopen
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
'''
'''
# 示例1的修改
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj.div)# head/ title/ h1/ div
'''

# 检查和错误处理
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError
def getTitle(url):
    try:
        html = urlopen(url)
    except(HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.h1 #bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if (title == None):
    print("title could not be found")
else:
    print(title)