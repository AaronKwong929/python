from selenium import webdriver
import time
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/question/24728633'
browser.get(url)
browser.implicitly_wait(10)

title = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1').text
browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/button').click()
brief = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/span').text
follower = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/strong').text
read = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/strong').text
'''
answerers = browser.find_elements_by_class_name('UserLink-link')  # 此段可行
print('问题：' + title + '\n简介：' + brief + '\n关注者：' + follower + '\n被浏览：' + read + '\n回答者：' )
for answerer in answerers:  #输出所有回答人，但动态加载滚动网页时除了硬等(time.sleep())没有其他办法 目前只能爬出第一次加载网页的几个人
    print(answerer.text)'''
answers = browser.find_elements_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span/p')

'''print('问题：' + title + '\n简介：' + brief + '\n回答者：')
for answerer, answer in zip(answerers, answers):
    print(answerer.text + '  ' + answer.text)
'''
for answer in answers:
    print(answer.text)
browser.quit()

# 爬答案正文爬不完全 --> 知乎 的排版有毒，
# //*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/span/p
# //*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/span/text()
# 这是一个回答下文字的两种xpath路径，分开爬不现实，不知道加一个try模块实不实用
#                                                           ↑↑
#                                                 这是第几个回答的数字，去掉之后直接爬了全部答案，
# 输出排版又成了问题，print(answer.text) 的话直接将所有回答放出来了，不能 "回答人：答案" 的样式显示出来