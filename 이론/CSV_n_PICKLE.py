# -*- coding: utf-8 -*-

# MARK: Read all CSV files
import glob, csv

files = glob.glob('data/class_score_??.csv')    # files에 class_score_en, class_score_kr 파일을 가져와 저장함
all_data = []
for file in files:
    with open(file, 'r') as f:  # file obj 생성
        csv_reader = csv.reader(f)  # csv reader obj 생성
        data = []   # 하나의 파일에 해당하는 data를 모아줄 리스트
        for line in csv_reader:
            if line and not line[0].strip().startswitch('#'):   # 주석이 아니라면
                data.append([int(val) for val in line])
            all_data += data
            

# MARK: Pickle
"""
파이썬의 data들을 file로 내보내거나 가져오고 싶을 때,
변수들을 그대로 저장해 사용할 수 있는 클래스임. (= 덩어리로 쓸 수 있음)
즉 Selialization 하는 것~
그렇기 때문에 파이썬 객체를 파일 형식에 관계 없이 save & load 할 수 있다.
"""
# MARK: Writing data to a file 
import pickle 
with open('class_score_all.pickle', 'wb') as f: 
    pickle.dump((files,all_data), f)    # 저장할 변수를 tuple로 넣음 
# MARK: Loading data from the file 
with open('class_score_all.pickle', 'rb') as f:
    _, data = pickle.load(f)    # 두 번째 것만 꺼내옴 
    print(data)
