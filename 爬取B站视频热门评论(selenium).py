from selenium import webdriver
import time

url = input('请输入B站视频链接：')
browser = webdriver.Firefox()
browser.maximize_window()
# url = 'https://www.bilibili.com/video/av5067136?from=search&seid=17107287613613241939'
browser.get(url)
browser.implicitly_wait(10)
time.sleep(5)
target = browser.find_element_by_xpath('//*[@id="comment"]/div/div[1]/span[2]')  # 找到评论
browser.execute_script("arguments[0].scrollIntoView();", target)  # 页面滚动到评论的位置后网页自动加载评论内容

target2 = browser.find_element_by_xpath('//*[@id="comment"]/div/div[2]/div[1]/div[4]/div[4]/span/a')  # 找到查看更多
browser.execute_script("arguments[0].scrollIntoView();", target2)  # 滚动到
time.sleep(2)
target2.click()  # 点击查看更多，加载热门评论

try:
    names = browser.find_elements_by_xpath('//*[@id="comment"]/div/div[2]/div[1]/div[4]/div/div[2]/div[1]/a[1]')
    contents = browser.find_elements_by_xpath('//*[@id="comment"]/div/div[2]/div[1]/div[4]/div/div[2]/p')
    for name, content in zip(names, contents):
        print(name.text.strip() + '  ' + content.text.strip() + '\n\n')
except IOError:
    pass

browser.quit()