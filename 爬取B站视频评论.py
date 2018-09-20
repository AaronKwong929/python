from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.maximize_window()
url = 'https://www.bilibili.com/video/av5067136?from=search&seid=17107287613613241939'
browser.get(url)
browser.implicitly_wait(10)
time.sleep(10)
target = browser.find_element_by_xpath('//*[@id="comment"]/div/div[1]/span[2]')
browser.execute_script("arguments[0].scrollIntoView();", target)

target2 = browser.find_element_by_xpath('//*[@id="comment"]/div/div[2]/div[1]/div[4]/div[4]/span/a')
browser.execute_script("arguments[0].scrollIntoView();", target2)
time.sleep(2)
target2.click()

try:
    names = browser.find_element_by_xpath('//*[@id="comment"]/div/div[2]/div[1]/div[4]/div/div[2]/div[1]/a[1]')
    contents = browser.find_element_by_xpath('//*[@id="comment"]/div/div[2]/div[1]/div[4]/div/div[2]/p')
    # print(names.text.strip(), contents.text.strip())
    time.sleep(2)
except IOError:
    pass
name = list(names)
content = list(contents)
print(name[0].text.strip())
print()
print(content[0].text.strip())
'''print(names)
print()
print(contents)'''
browser.quit()