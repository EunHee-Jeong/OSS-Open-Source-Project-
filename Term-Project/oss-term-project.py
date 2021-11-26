import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1-1. 데이터 불러오기
bus_data = pd.read_csv("./data/BUS_STATION_BOARDING_MONTH_202110.csv", encoding = 'cp949')
bus_data.head()
bus_data.info()

# 1-2. 확인하기 (필요한 데이터만, 오름차순 정렬)
sorted(list(set(bus_data['노선번호'])))
sorted(list(set(bus_data['노선명'])))
sorted(list(set(bus_data['역명'])))
sorted(list(set(bus_data['승차총승객수'])))
sorted(list(set(bus_data['하차총승객수'])))
