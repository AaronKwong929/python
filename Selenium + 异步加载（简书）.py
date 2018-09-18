from selenium import webdriver
url = 'https://www.jianshu.com/p/c9bae3e9e252'


def get_info(url):
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(20)
    author = browser.find_element_by_xpath('//span[@class="name"]/a').text
    date = browser.find_element_by_xpath('//span[@class="publish-time"]').text
    word = browser.find_element_by_xpath('//span[@class="wordage"]').text
    view = browser.find_element_by_xpath('//span[@class="views-count"]').text
    comment = browser.find_element_by_xpath('//span[@class="comments-count"]').text
    likes = browser.find_element_by_xpath('//span[@class="likes-count"]').text
    # rewards = browser.find_element_by_xpath('//span[@class="rewards-count"]').text  # 无法爬取???
    print(author, date, word, view, comment, likes)  # 无法输出赞赏数？？？？
    browser.quit()  # 不写会报错，quit()取代 close()


if __name__ == '__main__':
    get_info(url)