from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://www.qq.com/'
browser.get(url)
browser.implicitly_wait(20)

national_titles = browser.find_elements_by_xpath('//*[@id="newsInfoQuanguo"]/div/div/ul/li/a')
print("全国：")
for national_title in national_titles:
    print(national_title.text)

today_top_title = browser.find_element_by_xpath('//*[@id="todaytop"]/a').text
today_titles = browser.find_elements_by_xpath('//*[@id="today"]/div[2]/ul/li/a')
print("\n今日：")
print('头条：' + today_top_title)
for today_title in today_titles:
    print(today_title.text)

other_styles = browser.find_elements_by_xpath('//*[@id="aoyunshike"]/div[2]/ul/li/a[1]')
other_titles = browser.find_elements_by_xpath('//*[@id="aoyunshike"]/div[2]/ul/li/a[2]')
print('\n其他：')
for other_style, other_title in zip(other_styles, other_titles):
    print(other_style.text + '  ' + other_title.text)

entertainment_top_title = browser.find_element_by_xpath('//*[@id="ent"]/div[2]/div[1]/div[2]/h3/a').text
entertainment_titles = browser.find_elements_by_xpath('//*[@id="ent"]/div[2]/div/ul/li/a')
print('\n娱乐|明星|电影：')
print('头条：' + entertainment_top_title)
for entertainment_title in entertainment_titles:
    print(entertainment_title.text)

# 其余内容以此类推
browser.quit()