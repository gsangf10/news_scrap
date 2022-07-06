from konlpy.tag import Okt
import file_manager as fm
from collections import Counter

ok = Okt()

file_path = "C:/g_py/scrap/data/KBS_new_bodies.json"
bodies = fm.load_json(file_path)

result_list = []

for target in bodies :
    word_list = []
    for word, tag in ok.pos(target['body']) :
        if tag in ['Adjective', 'Noun', 'Verv'] :
            word_list.append(word)        

    counts = Counter(word_list)
    
    keyword_list = []
    for key, value in counts.items() :
        keyword = {
            "nid" : target['nid'],
            "word" : key,
            "cnt" : value
        }
        keyword_list.append(keyword)
    
    result_list.extend(keyword_list)
        
file_path = "C:/g_py/scrap/data/news_keyword.json"
fm.save_json(file_path, result_list)

word_list = []
for word, tag in ok.pos(target['body']) :
    if tag in ['Adjective', 'Noun', 'Verv'] :
        word_list.append(word)        

counts = Counter(word_list)

tags = counts.most_common(50)
print(dict(tags))

# wordcloud로 단어별 시각화
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(font_path="C:/Windows/Fonts/MALGUN.TTF", background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

plt.axis("off")
plt.imshow(cloud)
plt.show()