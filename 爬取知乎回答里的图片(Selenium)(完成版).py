from selenium import webdriver
import urllib.request
import time
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.zhihu.com/question/29815334'
browser.get(url)
# 登陆
# browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/div[1]/div[2]/div/div/button[1]').click()
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').clear()
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys('15521603459')
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').clear()
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('Kuangjunhao929')
# browser.find_element_by_xpath('').click()

# 知乎反爬验证,一直出Missing argument grant_type，解决方法：自己手动扫码登陆

print('进入30秒等待时间。')
time.sleep(30)
print('刷新网页。')
browser.refresh()
print('进入10秒隐式等待时间。')
browser.implicitly_wait(10)

# 开始爬图
print('开始爬图。')
src_links = []  # 列表存放src链接
img_infos = browser.find_elements_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div/div/div[2]/div[1]/span/figure/img')
for img_info in img_infos:
    time.sleep(1)  # 反反爬
    src_link = img_info.get_attribute('src')
    src_links.append(src_link)

browser.quit()

# 文件写入
count = 0
for src_link in src_links:
    f = open("C:/Users/Arron/Desktop/photo/" + str(count) + ".jpg", 'wb')
    f.write((urllib.request.urlopen(src_link)).read())
    f.close()
    print('第' + str(count) + '张图片已爬取。')
    count += 1
    

# 无法用selenium模拟鼠标滚动
# 使用time.sleep(20) 手动动态加载
# 知乎要先做一个登陆才能看到刺激的图片