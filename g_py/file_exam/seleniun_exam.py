from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('C:/g_py/chrome_driver/chromedriver.exe')
driver.get("https://media.naver.com/press/023/ranking?type=popular")

btn = driver.find_element(By.CLASS_NAME, 'button_date_prev')

for i in range(4):
    # driver.implicitly_wait(10)
    time.sleep(1)
    btn.click()

# navs = driver.find_elements(By.CLASS_NAME, 'nav_item')

# target = None
# for nav in navs:
#     if nav.text == '카페':
#         target = nav
        
# if target != None:
#     target.click()

# driver.implicitly_wait(10) # 문서가 다 로드 되기까지 대기, 최대 10초 까지

# input_txt = driver.find_element(By.CLASS_NAME, 'input_text')
# input_txt.send_keys('고양이')

time.sleep(10)