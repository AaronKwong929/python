from selenium import webdriver
import urllib.request
import time
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.zhihu.com/question/29815334'
browser.get(url)
time.sleep(10)
src_links = []
img_infos = browser.find_elements_by_xpath(
    '//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span/figure/img'
)
for img_info in img_infos:
    time.sleep(1)
    src_link = img_info.get_attribute('src')
    src_links.append(src_link)

browser.quit()

count = 0
for src_link in src_links:
    f = open("C:/Users/Arron/Desktop/photo/" + str(count) + ".jpg", 'wb')
    f.write((urllib.request.urlopen(src_link)).read())
    f.close()
    count += 1

# 无法用selenium模拟鼠标滚动
# 使用time.sleep(20) 手动动态加载
# 知乎要先做一个登陆才能看到刺激的图片