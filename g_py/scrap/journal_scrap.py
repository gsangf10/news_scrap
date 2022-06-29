from bs4 import BeautifulSoup   # html 형식으로 작성된 문자열을 html 구조로 파싱하기 위한 모듈
import requests                 # 특정 서버에 웹요청을 보내기 위한 모듈

url = 'https://news.naver.com/main/ranking/popularDay.naver'    # 네이버 뉴스랭킹 페이지

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

# 그룹별 언론사 리스트 가져오기
def get_journal_list_by_group(gid):
    soup = get_soup()
    tags = soup.find(attrs={'class' : gid})
    alist = tags.find_all(attrs={'class' : 'rankingnews_box'})

    journal_list = []
    for tag in alist:
        journal_list.append(get_journal(tag))
    
    return journal_list

# 
def get_journal_id(link):
    idx = link.rfind('/')   # rfind() - 특정 문자를 뒤에서부터 찾기
    jid = link[idx-3:idx]
    
    return jid

# 언론사 정보 구조화하기
def get_journal(tag):
    a = tag.find('a')
    strong = a.find('strong')
    name = strong.text
    link = a['href']

    jid = get_journal_id(link)

    journal = {
        'id' : jid,
        'name' : name,
        'link' : link
    }
    
    return journal

# 각 언론사 그룹 아이디 가져오기
def get_group_id_list(tags):
    group_id_list = []
    for tag in tags :    
        group_id = tag['class'][0] + " " + tag['class'][1]
        group_id_list.append(group_id)
        
    return group_id_list

# 모든 그룹의 언론사 가져오기
def get_all_journal_list():
    soup = get_soup()
    tags = soup.find_all(attrs={'class' : '_officeCard'})
    glist = get_group_id_list(tags)
    
    journal_list = []
    for gid in glist :
        journal_list.extend(get_journal_list_by_group(gid))
    
    return journal_list 

# 언론사 리스트 출력 포맷
def print_journal_list(journal_list):
    for j in journal_list:
        print(f"번호 : {j['id']}")
        print(f"이름 : {j['name']}")
        print(f"링크 : {j['link']}")
        print("===============")

journal_list = get_all_journal_list()
journal_list.sort(key = lambda el : el['id'])
# print_journal_list(journal_list)