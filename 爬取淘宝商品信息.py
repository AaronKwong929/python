from selenium import webdriver
from lxml import etree
import time


driver = webdriver.Chrome()
driver.maximize_window()


def nextPage(url, page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(3)
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    getInfo(driver.current_url, page)


def getInfo(url, page):
    page += 1
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        try:
            data = info.xpath('div/div/a')[0]  # 111
            goods = data.xpath('string(.)').strip()  # 222
            price = info.xpath('div[2]/div[1]/div[1]/strong/text()')[0]
            sold = info.xpath('div/div/div[@class="deal-cnt"]/text()')[0]  # 两层div
            shop_name = info.xpath('div[2]/div[3]/div[1]/a/span[2]/text()')[0]
            location = info.xpath('div[2]/div[3]/div[2]/text()')[0]
            print(price + '  ' + sold + '  ' + goods + '  ' + shop_name + '  ' + location)
        except IndexError:
            pass
    if page < 3:
        nextPage(url, page)
    else:
        pass


if __name__ == "__main__":
    page = 1
    url = 'https://www.taobao.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')
    driver.find_element_by_class_name('btn-search').click()
    getInfo(driver.current_url, page)
