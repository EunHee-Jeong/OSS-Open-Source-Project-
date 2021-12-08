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

# 2-2. 노선별 평균 승하차 인원 확인
bus_st = my_bus_data.groupby(['노선번호','역명']).mean().reset_index()
bus_st

# 2-3. 상위 5개 노선 출력
bus_st = bus_st.sort_values(by = '승차총승객수', ascending = False) # 승하차가 비례함을 확인했기 때문에, 승차총승객수를 기준으로 잡음
bus_st.head(5)

# 2-4. 202번 버스의 승차 인원 컬럼만 추출
num = '202'
bus_st_202 = bus_st[bus_st['노선번호']==num]
bus_get_on = pd.DataFrame()
bus_get_on['노선번호'] = bus_st_202['노선번호']
for i in range(int((len(my_bus_data.columns)-3)/2)):
    bus_get_on[bus_st_202.columns[3+2*i]] = bus_st_202[bus_st_202.columns[3+2*i]]
bus_get_on = bus_get_on.set_index('노선번호')
bus_get_on

# 2-5. 202번 버스의 하차 인원 컬럼만 추출
bus_get_off = pd.DataFrame()
bus_get_off['노선번호'] = bus_st_202['노선번호']
for i in range(int((len(my_bus_data.columns)-3)/2)):
    bus_get_off[bus_st_202.columns[4+2*i]] = bus_st_202[bus_st_202.columns[4+2*i]]
bus_get_off = bus_get_off.set_index('노선번호')
bus_get_off


# 3-1. 데이터 프레임으로 저장
df = pd.DataFrame(index = bus_st_202['역명'])
df['평균 승차 인원 수'] = bus_get_on.mean(axis=0).astype(int)
df['평균 하차 인원 수'] = bus_get_off.mean(axis=0).astype(int)
df

# 3-2. 막대그래프 형태로 시각화
df.plot.bar()
