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
'''
# 检查和错误处理
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError
def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
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
'''
'''
#findall()实例
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")
nameList = bsObj.findAll("span", {"class":{"green"}}) # 抽取<span class="green></span>里的文字    # find(),findall()
for name in nameList:
    print(name.get_text()) # print(name)保留所有html标签
'''
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")
nameList = bsObj.findAll(text = "the prince")
# nameList = bsObj.findAll("",{"text":"the prince"})  # 不能使用
print(nameList)
'''
'''
# find（）子标签后代标签兄弟标签
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
for child in bsObj.find("table",{"id":"giftList"}).children: # 子标签，父标签的下一级
    print(child)
for descend in bsObj.find("table",{"id":"giftList"}).descendants: # 后代标签，父标签的下面所有级别的标签
    print(descend)
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:# next_sibling:返回单个标签。同样的有previous_siblings/previous_sibling
    print(sibling)
'''

# 正则表达式： 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
    