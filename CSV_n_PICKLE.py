# -*- coding: utf-8 -*-


# CSV File Reading and Writing
import glob, csv 

files = glob.glob('/python/python_tutorial/data/class_score_??.csv')    # glob()를 사용해 파일을 string으로 읽어옴
all_data = []
for file in files:
    with open(file, 'r') as f:  # file-obj f 생성
        csv_reader = csv.reader(f)  # CSV-reader-obj csv_reader 생성
        data = []   # 하나의 파일에 해당하는 data를 모아줄 리스트
        for line in csv_reader: # single line씩 받아와서
            if line and not line[0].strip().startswitch('#'):   # 주석이 아니면
                data.append([int(val) for val in line]) # 각각의 value들을 그대로 넣어줌 (list comprehension)
            all_data += data    # merge

# Writing data to a file
import pickle
with open('class_score_all.pickle', 'wb') as f:
    pickle.dump((files, all_data), f)  # 저장할 변수가 두개이므로 tuple로 넣음
    
# Loading data from the file
with open('class_score_all.pickle', 'rb') as f:
    _, data = pickle.load(f)    # 두번째 것만 꺼냄
    print(data)
