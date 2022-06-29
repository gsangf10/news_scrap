import csv

# 1. csv 쓰기 1
with open('file_exam/exam_data/exam_1.csv', 'w', encoding='utf-8-sig') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow([1,2,3,4])
    csv_writer.writerows([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    

# 2. csv 쓰기 2
with open('file_exam/exam_data/exam_2.csv', 'w', encoding='utf-8-sig') as f:
    dict_writer = csv.DictWriter(f, fieldnames=['name', 'age', 'home'])
    dict_writer.writeheader()
    dict_writer.writerow({'name':'hong', 'age':30, 'home':'seoul'})
    dict_writer.writerow({'name':'hwang', 'age':35, 'home':'daejeon'})


# 1. csv 읽기 1
with open('file_exam/exam_data/exam_1.csv', 'r', encoding='utf-8-sig') as f:
    csv_reader = csv.reader(f, delimiter=',')
    csv_list = list(csv_reader)
    print(csv_list)
    

# 2. csv 읽기 2
with open('file_exam/exam_data/exam_2.csv', 'r', encoding='utf-8-sig') as f:
    csv_reader = csv.DictReader(f, fieldnames=['name', 'age', 'home'])
    # csv_dict = dict(csv_reader)
    print(csv_reader)