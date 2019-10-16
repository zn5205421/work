# coding=UTF-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary as browser_bin
import logging

logging.basicConfig(level = logging.DEBUG,filename ='selenium.log', filemode ='w', format='%(name)s-%(levelname)s -%(message)s')

search_inbox_id = 'sb_form_q'
search_button_id = 'sb_form_go'

# driver = webdriver.Chrome('driver/chromedriver.exe')
driver = webdriver.Chrome(browser_bin.chromedriver_filename)

driver.get('https://www.bing.com')

logging.debug('home page opened')

driver.maximize_window()
driver.save_screenshot('screenshot/home.png')

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'sb_form_q')))

time.sleep(4)
#定位输入框并输入内容
driver.find_element_by_id(search_inbox_id).clear()
time.sleep(2)
#清空输入框
driver.find_element_by_id(search_inbox_id).send_keys('kk')
driver.find_element_by_id(search_inbox_id).screenshot('screenshot/textbox.png')
time.sleep(2)
#重新输入
#driver.find_element_by_id(search_button_id).click()
driver.find_element_by_id(search_button_id).send_keys(Keys.ENTER)
#点击搜索
#driver.find_element_by_link_text('kk').click()
#文本定位
assert driver.title.__contains__('kk')
driver.quit()

