from selenium import webdriver
import time
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/question/24728633'
browser.get(url)
browser.implicitly_wait(10)

title = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1').text
browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/button').click()
brief = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/span').text
answerers = browser.find_elements_by_class_name('UserLink-link')
print('问题：' + title + '\n简介：' + brief + '\n回答者：')
for answerer in answerers:
    print(answerer.text)
# answers = browser.find_elements_by_class_name('RichText ztext CopyrightRichText-richText')
'''print('问题：' + title + '\n简介：' + brief + '\n回答者：')
for answerer, answer in zip(answerers, answers):
    print(answerer.text + '  ' + answer.text)
'''
browser.quit()