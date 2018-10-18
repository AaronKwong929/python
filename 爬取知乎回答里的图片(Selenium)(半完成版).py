from selenium import webdriver
import urllib.request
import time
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.zhihu.com/question/29815334'
browser.get(url)
# 登陆不可以进行自动化输入，会出现Missing argument grant_type，解决方法：自己手动扫码登陆
# browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/div[1]/div[2]/div/div/button[1]').click()
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').clear()
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys('15521603459')
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').clear()
# browser.find_element_by_xpath('/html/body/div[7]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('Kuangjunhao929')
# browser.find_element_by_xpath('').click()

print('进入30秒等待时间。')  # 用于扫码登陆
time.sleep(30)
print('刷新网页。')
browser.refresh()
print('进入10秒隐式等待时间。')
browser.implicitly_wait(10)

# 滚动网页的正确解法↓
for i in range(1000):
    # browser.execute_script('window.scrollTo(0,1000000)')  #这个方法可以激活动态加载但不能获取跳过区间图片的src链接
    browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[2]/div/div/div[1]/button[1]').send_keys(Keys.ARROW_DOWN)
    # 定位网页上端的按钮，模拟键盘方向键↓操作1000次，可以激活动态加载和获取src
# 开始爬图
print('开始爬图。')
src_links = []  # 列表存放src链接
img_infos = browser.find_elements_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div/div/div[2]/div[1]/span/figure/img')
for img_info in img_infos:
    time.sleep(1)  # 反反爬
    src_link = img_info.get_attribute('src')
    src_links.append(src_link)
browser.quit()

print('一共获取到：' + str(len(src_links)) + '张图片。')
# 文件写入
count = 0
for src_link in src_links:
    f = open("C:/Users/Arron/Desktop/photo/" + str(count) + ".jpg", 'wb')
    f.write((urllib.request.urlopen(src_link)).read())
    f.close()
    print('第' + str(count) + '张图片已爬取。')
    count += 1
    
# 暂时没有做出知乎登陆的自动化操作