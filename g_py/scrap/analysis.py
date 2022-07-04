import pandas as pd

# 1. json 파일을 이용해서 데이터프레임 만들기
file_path1 = '/content/KBS.json'
kbs = pd.read_json(file_path1, orient='records', encoding='utf-8-sig')

file_path2 = '/content/MBC.json'
mbc = pd.read_json(file_path2, orient='records', encoding='utf-8-sig')

file_path3 = '/content/SBS.json'
sbs = pd.read_json(file_path3, orient='records', encoding='utf-8-sig')

file_path4 = '/content/KBS_comment.json'
kbs_comm = pd.read_json(file_path4, orient='records', encoding='utf-8-sig')

file_path5 = '/content/MBC_comment.json'
mbc_comm = pd.read_json(file_path5,  orient='records', encoding='utf-8-sig')

file_path6 = '/content/SBS_comment.json'
sbs_comm = pd.read_json(file_path6, orient='records', encoding='utf-8-sig')

# 2. 같은 구조의 데이터 프레임 합치기 (concat)
all_news = pd.concat((kbs, mbc), ignore_index=True)
all_news = pd.concat((all_news, sbs), ignore_index=True)

all_comm = pd.concat((kbs_comm, mbc_comm), ignore_index=True)
all_comm = pd.concat((all_comm, sbs_comm), ignore_index=True)

all_news.head(5)
all_comm.head(5)

# 3. 다른 구조의 데이터 프레임 합치기 (merge)
all_news
all_comm

rst = pd.merge(all_news, all_comm, how='left', left_on='nid', right_on='번호')

rst2 = rst[['nid','link', '댓글수', '남자', '여자']]
rst2

# 4. 다양한 분석 시도.

# 4-1. 20대가 가장 많이 본(댓글을 많이 작성한) 뉴스 (언론사, 뉴스 번호, 타이틀, 링크)
rst2 = rst.sort_values('20대').head(1) 
rst2[['jid', 'nid', 'title', 'link']]

# 4-2. 가장 댓글이 적은 뉴스의 댓글 수와 뉴스 링크, 뉴스 번호
rst['댓글수(int)'] = rst['댓글수']

# 0 - False, 1 - True
# 결측치 개수 구하기
# isna() 특정 컬럼 또는 데이터프레임의 결측치를 찾아줌
rst['댓글수(int)'].isna().sum()

# fillna() - 결측치를 특정 값으로 채움

rst2 = rst['댓글수(int)'].str.replace(',', '')

rst2 = rst2.fillna(0)
rst2

rst2 = rst2.astype('int64')

rst2
rst['댓글수(int)'] = rst2
rst

rst.sort_values('댓글수(int)')[['nid', 'link', '댓글수(int)']].head(1)

# 4-3. 언론사 번호와 언론사 이름으로 구성된 데이터 프레임을 만들고 merge를 이용해 각 뉴스에 언론사 이름을 붙여주기

jids = rst['jid'].unique()
names = [ 'KBS', 'MBC', 'SBS' ]
data1 = {
    
    'jid' : jids, 
    'name' : names
}

jnames = pd.DataFrame(data1)

rst2 = pd.merge(jnames, rst, how='right', on='jid')
rst2

# 4-4. 각 언론사별 평균 댓글 수(댓글 수로 내림차순 정렬)
rst3 = rst2.groupby(['name']).mean()[['댓글수(int)']]

rst3 = rst3.rename(columns={'댓글수(int)' : '평균댓글수'})
rst3 = rst3.sort_values('평균댓글수', ascending=False)
rst3

# 4-5. 여성의 댓글수가 가장 많은 언론사

rst4 = rst['여자'].str.replace('%', '')

rst4 = rst4.fillna(0)

rst4 = rst4.astype('int64')

rst2['여자(int)'] = rst4

rst4 = rst2.groupby('name').mean('여자(int)').sort_values('여자(int)', ascending=False).head(1)
rst4

# 4-6. 각 언론사 별 댓글을 많이 작성한 연령대 top3

rst5 = rst2.loc[:, '10대' : '60대↑']

def remove_percent(row) :
  for i, val in enumerate(row) :
    if str(type(val)) == "<class 'str'>" :
      row[i] = val.replace('%', '')
  row = row.fillna(0).astype('int64')
  return row

rst6 = rst5.apply(remove_percent, axis=1)
rst2.loc[:, '10대' : '60대↑'] = rst6

rst7 = rst2.groupby('name').sum().loc[:, '10대': '60대↑']

def get_top_three(row) :
  row = row.sort_values(ascending=False)
  row = row[:3].index
  row = pd.Series(row, index=['1위', '2위', '3위'])
  return row

rst8 = rst7.apply(get_top_three, axis=1)
rst8 

# 또는

rst8.reset_index().rename(columns={'name' : 'rank'}).set_index('rank').T