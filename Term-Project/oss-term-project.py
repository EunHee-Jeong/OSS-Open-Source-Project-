import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1-1. 데이터 불러오기
bus_data = pd.read_csv("./drive/MyDrive/data/BUS_STATION_BOARDING_MONTH_202110.csv", encoding = 'cp949')
bus_data.head()
bus_data.info()

# 1-2. 확인하기 (필요한 데이터만, 오름차순 정렬)
sorted(list(set(bus_data['노선번호'])))
sorted(list(set(bus_data['노선명'])))
sorted(list(set(bus_data['역명'])))
sorted(list(set(bus_data['승차총승객수'])))
sorted(list(set(bus_data['하차총승객수'])))

# 2-1. 불필요한 칼럼 제거
my_bus_data = bus_data.drop(columns={'버스정류장ARS번호', '등록일자'})
my_bus_data

# 2-2. 202번 버스의 승차 인원 컬럼만 추출
num = '202'
bus_st_202 = bus_st[bus_st['노선번호']==num]
bus_get_on = pd.DataFrame()
bus_get_on['노선번호'] = bus_st_202['노선번호']
for i in range(int((len(my_bus_data.columns)-3)/2)):
    bus_get_on[bus_st_202.columns[3+2*i]] = bus_st_202[bus_st_202.columns[3+2*i]]
bus_get_on

# 2-3. 202번 버스의 하차 인원 컬럼만 추출
num = '202'
bus_st_202 = bus_st[bus_st['노선번호']==num]
bus_get_off = pd.DataFrame()
bus_get_off['노선번호'] = bus_st_202['노선번호']
for i in range(int((len(my_bus_data.columns)-3)/2)):
    bus_get_off[bus_st_202.columns[4+2*i]] = bus_st_202[bus_st_202.columns[4+2*i]]
bus_get_off

# 2-4. 노선별 평균 승하차 인원 추출하기
bus_st = my_bus_data.groupby(['노선번호','역명']).mean().reset_index()
bus_st
