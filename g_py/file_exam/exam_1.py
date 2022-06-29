txt = '코코콬코'

# 1. 파일 저장
f = open('file_exam/exam_data/test.txt', 'w', encoding='utf-8-sig')

f.write(txt)
# 문자열 여러개 저장
f.writelines(['aaa\n', 'bbb\n', 'ccc\n'])

f.close()

f2 = open('file_exam/exam_data/test.txt', 'a', encoding='utf-8-sig')
f2.write('새로운 내용')

f2.close()

# 2. 파일 읽기
f3 = open('file_exam/exam_data/test.txt', 'r', encoding='utf-8-sig')

txt1 = f3.read() # 전체 읽어오기
print(txt1)

f3.seek(0) # 커서 초기화

txt3 = f3.readline() # 전체 읽어오기
print(txt3)

f3.close()

with open('file_exam/exam_data/test.txt', 'r', encoding='utf-8-sig') as f4:
    print(f4.read())
    
# 문제
# 1. 고양이, 강아지, 오리, 원숭이, 악어 줄바꿈해서 파일에 저장
# 2. 오리와 원숭이 사이에 말 저장

s_list = ['고양이\n', '강아지\n', '오리\n', '원숭이\n', '악어\n']

with open('file_exam/exam_data/exam_1.txt', 'w', encoding='utf-8-sig') as f:
    f.writelines(s_list)


with open('file_exam/exam_data/exam_1.txt', 'a', encoding='utf-8-sig') as f:
    f.write('말\n')