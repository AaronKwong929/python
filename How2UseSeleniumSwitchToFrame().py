# 参考：https://blog.csdn.net/huilan_same/article/details/52200586
'''
<html lang="en">
<head>
    <title>FrameTest</title>
</head>
<body>
<iframe src="a.html" id="frame1" name="myframe"></iframe>
</body>
</html>
'''
# 切进frame1
'''
from selenium import webdriver
driver = webdriver.Firefox()
driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
# driver.switch_to.frame("frame1")  # 2.用id来定位
# driver.switch_to.frame("myframe")  # 3.用name来定位
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
'''
# 返回
'''
driver.switch_to.default_content()
'''
# 嵌套
'''
<html>
    <iframe id="frame1">
        <iframe id="frame2" / >
    </iframe>
</html>
'''
'''
driver.switch_to.frame("frame1")
driver.switch_to.frame("frame2")
'''
#在frame2 切回frame1
'''
driver.switch_to.parent_frame()  # 如果当前已是主文档，则无效果
'''