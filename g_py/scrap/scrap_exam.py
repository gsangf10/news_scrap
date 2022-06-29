from bs4 import BeautifulSoup   # html 형식으로 작성된 문자열을 html 구조로 파싱하기 위한 모듈
import requests     # 특정 서버에 웹요청을 보내기 위한 모듈

# 1. 특정 페이지로 요청보내서 html 문서 받아오기.
url = 'https://www.naver.com'

res = requests.get(url)     # url에 요청 보내서 요청에 대한 응답 리턴
html = res.text    # 응답 결과의 문서

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())