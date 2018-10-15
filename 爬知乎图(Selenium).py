from selenium import webdriver
import urllib.request
import time
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.zhihu.com/question/29815334'
browser.get(url)
browser.implicitly_wait(20)
js = "var q=document.documentElement.scrollTop=2400"
browser.execute_script(js)
browser.implicitly_wait(20)
time.sleep(20)

img_set = browser.find_element_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span/figure/img')
print(img_set.get_attribute('src'))
img_path = img_set.get_attribute('src')

f = open("C:/Users/Arron/Desktop/photo/" + str('test')+".jpg", 'wb')
f.write((urllib.request.urlopen(img_path)).read())
f.close()
browser.quit()

# 正常语法下xpath应该为'//xxxx/xxx/xx/x/@href'
# selenium下用xpath获取内容后获取属性的方法--> xxx = .find_element_by_x   xxx.get_attribute('href') 
# https://blog.csdn.net/hacklyc/article/details/65454285
