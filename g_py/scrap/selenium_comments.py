from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium_news as ns

import time

url = ""

def set_url(url_param) :
    global url
    url = url_param
    
def get_driver() :    

    global url

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('C:/g_py/chrome_driver/chromedriver.exe', options=options)
    driver.get(url)

    return driver

# 댓글수, 성별정보, 나이대정보
def get_comment_info(news):
    
    domain = "https://n.news.naver.com/article/comment/"
    link = news['j_id'] + "/" + news['n_id']
    
    link = domain + link 
    
    set_url(link)
    driver = get_driver()
    
    elmt = driver.find_element(By.ID, "cbox_module")
    # time.sleep(1)
    
    try:
        btn = driver.find_element(By.CLASS_NAME, "is_navercomment")
        btn.click()
        driver.implicitly_wait(10)
    except:
        return None
        
    n_id = ns.get_news_id(news['link'])
    cnt = get_comment_cnt(elmt)
    
    if int(cnt) < 100:
        chart_sex = ''
        chart_age = ''
    else:
        chart_sex = get_chart_sex(elmt)
        chart_age = get_chart_age(elmt)
    
    comment_info = {}
    comment_info["번호"] = n_id
    comment_info["댓글수"] = cnt
    comment_info.update(chart_sex)
    comment_info.update(chart_age)
    
    return comment_info
    
def get_comment_cnt(elmt):
    span = WebDriverWait(elmt, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_count'))
    )
    
    if span != None:
        return span.text
    
    return '태그가 존재하지 않습니다'

def get_chart_sex(elmt):
    chart_sex = WebDriverWait(elmt, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_chart_sex"))
    )
    
    chart_progresses = chart_sex.find_elements(By.CLASS_NAME, 'u_cbox_chart_progress')
    
    result = {}
    for progress in chart_progresses :            
        p_key = progress.find_element(By.CLASS_NAME, 'u_cbox_chart_cnt').text
        p_value = progress.find_element(By.CLASS_NAME, 'u_cbox_chart_per').text
        result[p_key] = p_value
    return result
    
def get_chart_age(elmt):
    chart_age = WebDriverWait(elmt, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_chart_age'))
    )
    
    age_progresses = chart_age.find_elements(By.CLASS_NAME, 'u_cbox_chart_progress')
    
    result = {}
    for progress in age_progresses:
        p_key = progress.find_element(By.CLASS_NAME, 'u_cbox_chart_cnt').text
        p_value = progress.find_element(By.CLASS_NAME, 'u_cbox_chart_per').text
        
        result[p_key] = p_value
        
    return result