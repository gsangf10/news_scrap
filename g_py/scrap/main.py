import imp
import journal_scrap as js
import news_scrap as ns
import file_manager as fm
import selenium_comments as sc

# 1. 언론사 목록 가져오기
j_list = js.get_all_journal_list()

# KBS, SBS, MBC 정보 가져오기
search_list = ['KBS','SBS','MBC']
journal = []
for j in j_list:
   if j['name'] in search_list:
       journal.append(j)

# 2. 언론사별 랭킹 뉴스 가져오기
for j in journal:
    news_list = ns.get_news_list_by_journal(j)

    # 3. 뉴스 목록을 JSON으로 파일 저장
    file_path = 'C:/g_py/scrap/data/' + j['name'] + '.json'
    fm.save_json(file_path, news_list)

    # 4. 뉴스의 댓글 통계 정보 가져오기
    news_list = fm.load_json(file_path)

    # 5. 각 뉴스의 댓글 정보 저장
    comments = []
    for news in news_list :
        comment_info = sc.get_comment_info(news)
        if comment_info :
            comments.append(comment_info)

    file_path = 'C:/g_py/scrap/data/' + j['name'] + '_comment.json'
    fm.save_json(file_path, comments)