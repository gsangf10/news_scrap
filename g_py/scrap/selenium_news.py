from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import journal_scrap as js

url = "https://media.naver.com/press/662/ranking?type=comment" 

def set_url(url_param) :
    global url
    url = url_param

def get_driver() :    

    driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe')
    driver.get(url)

    return driver

def get_news_id(link) :
    idx = link.rfind('/')   
    nid = link[idx + 1: idx + 11]  
    return nid

def get_new_list_by_journal(journal) :
    set_url(journal['link'])
    driver = get_driver()
    driver.implicitly_wait(10)
    
    btn = driver.find_element(By.CLASS_NAME, 'button_date_prev')
    
    btn.click()
    time.sleep(1)
    btn.click()
    time.sleep(3)
    
    ranking_list = driver.find_element(By.CLASS_NAME, 'press_ranking_list')
    ranking_news_list = ranking_list.find_elements(By.CLASS_NAME, 'as_thumb')
    
    my_news_list = []    
    
    
    for i, news in enumerate(ranking_news_list) :   
        if i == 5 :
            break 
        # 해당 뉴스가 어떤 언론사의 뉴스인지. 언론사번호
        global url
        jid = js.get_journal_id(url)
        print(jid)
        # 해당 뉴스의 링크
        a = news.find_element(By.TAG_NAME, 'a')
        link = a.get_attribute('href')
        print(link)
        
        # 해당 뉴스의 식별번호
        nid = get_news_id(link)
        
        # 해당 뉴스의 제목
        title = news.find_element(By.CLASS_NAME, 'list_title').text
        print(title)
        my_news = {
            'jid' : jid,
            'nid' : nid,
            'title' : title,
            'link' : link
        }
        
        my_news_list.append(my_news)
        
    return my_news_list