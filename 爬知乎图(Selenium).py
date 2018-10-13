from selenium import webdriver
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

img_set = browser.find_element_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span/figure/img[@src]')



browser.quit()