from bs4 import BeautifulSoup   # html 형식으로 작성된 문자열을 html 구조로 파싱하기 위한 모듈
import requests                 # 특정 서버에 웹요청을 보내기 위한 모듈
import journal_scrap as js

url = 'https://media.naver.com/press/437/ranking?type=popular'    # 네이버 뉴스랭킹 페이지

def set_url(url_param):
    global url
    url = url_param

# 특정 페이지로 요청보내서 html 문서 받아오기.
def get_soup():
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=header)     # url에 요청 보내서 요청에 대한 응답 리턴
    html = res.text                             # 응답 결과의 문서
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

# 해당 뉴스의 식별번호
def get_news_id(link):
    idx = link.rfind('/')
    news_id = link[idx+1:idx+11]
    
    return news_id

# 언론사의 뉴스 리스트 정보
def get_news_list_by_journal(journal):
    set_url(journal['link'])
    soup = get_soup()
    ranking_lists = soup.find_all(attrs={'class' : 'press_ranking_list'})
    
    result_list = []
    for ranking_list in ranking_lists :    
        ranking_news_list = ranking_list.find_all(attrs={'class' : 'as_thumb'})        
        news_list = get_news_list(ranking_news_list)
        result_list.extend(news_list)
        
    return result_list

# 해당 뉴스 정보
def get_news_info(news):
    global url
    soup = get_soup()
    
    # 해당 뉴스가 어떤 언론사인지
    j_id = js.get_journal_id(url)
    j_name = soup.find(attrs={'class':'press_hd_name_link'}).text.strip()
    
    # 뉴스 링크
    a = news.find('a')
    link = a['href']
    
    # 뉴스 식별번호
    n_id = get_news_id(link)
    
    # 뉴스 제목
    title = news.find(attrs={'class':'list_title'}).text
    
    news_dict = {
        'j_id' : j_id,
        'j_name' : j_name,
        'n_id' : n_id,
        'title' : title,
        'link' : link
    }
    
    return news_dict

# 뉴스 리스트 정보
def get_news_list(ranking_list):
    news_list = []
    for news in ranking_list:
        news_list.append(get_news_info(news))
    
    return news_list

# 뉴스 리스트 출력 포맷
def print_news_list(news_list):
    for news in news_list:
        print(f"언론사번호 : {news['j_id']}")
        print(f"언론사 : {news['j_name']}")
        print(f"뉴스번호 : {news['n_id']}")
        print(f"제목 : {news['title']}")
        print(f"링크 : {news['link']}")
        print("===============")