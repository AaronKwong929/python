from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
'''chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
'''
# browser = webdriver.Chrome('C:/Users/Arron/AppData/Local/Programs/Python/Python37-32/chromedriver.exe')
browser = webdriver.Chrome()
browser.get('http://www.douban.com/')
browser.implicitly_wait(10)
browser.find_element_by_id('form_email').clear()
browser.find_element_by_id('form_email').send_keys('##########')
browser.find_element_by_id('form_password').clear()
browser.find_element_by_id('form_password').send_keys('************')
browser.find_element_by_class_name('bn-submit').click()
print(browser.page_source)