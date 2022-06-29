# 간단한 주소록 저장 프로그램

import json 
import os

person_file_path = "file_exam/exam_data/person_json/"
person_no_file_path = "file_exam/exam_data/person_no/person_no.json"

def set_next_person_no(no):           
    with open(person_no_file_path, 'w', encoding='utf-8-sig') as f :
        no_dic = {
            "no" : no
        }             
        json_str = json.dumps(no_dic)        
        f.write(json_str)
        
    return 0

def get_person_no() :
    no = 1
    
    if not os.path.isfile(person_no_file_path) :
        set_next_person_no(no)
    else :        
        with open(person_no_file_path, 'r', encoding='utf-8-sig') as f :
            no_dic = json.load(f)
            no = no_dic['no'] + 1
            set_next_person_no(no)
            
    return no

while True :
    menu = input("메뉴 선택(1. 사람 추가 2. 목록 조회 3. 종료) :" )
    
    if menu == "1" :
        name = input("이름 : ")
        age = int(input("나이 : "))
        home = input("거주지 : ")
        
        person = {
            "name" : name,
            "age" : age,
            "home" : home
        }

        json_str = json.dumps(person, ensure_ascii=False)
        file = person_file_path + "person_" + str(get_person_no()) + ".json"
        with open(file, 'w', encoding='utf-8-sig') as f :
            f.write(json_str)
            
    elif menu == "2" :
        file_list = os.listdir(person_file_path)
        if len(file_list) == 0 :
            print('데이터가 없습니다.')
        else :
            for file in file_list :
                file = person_file_path + file
                with open(file, 'r', encoding='utf-8-sig') as f :
                    person = json.load(f)
                    print(f'이름 : {person["name"]}, 나이 : {person["age"]}, 거주지 : {person["home"]}')
    elif menu == "3" :
        break