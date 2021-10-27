# -*- coding: utf-8 -*-

def normalize_data(n_cases, n_people, scale):
    # TODO: Calculate the number of cases per its population
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append((float(n) / n_people[idx]) * scale)
        # 100만명 당 신규 확진 비율을 norm_cases 리스트에 저장함
        # (지역별 확진자 수 / 지역별 인구수) * 1000000
        # 비율은 소수로 나올 것이기 때문에 계산값을(둘 다 정수) 실수형으로 먼저 바꿔주고 계산하였음.
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227,  13530519, 3359527,     3322373,   2938429,     2630254, 2393626,    2118183,   1838353,   1792476,    1597179,   1536270,   1454679,   1441970, 1124459, 675883,   365309] # 2021-08
n_covid  = [    644,       529,      38,          29,       148,          28,      41,         62,        23,        27,         27,        33,        16,        40,      20,      5,        4] # 2021-09-21

sum_people = float(sum(n_people)) # TODO: The total number of people
            # 변수 sum_people에 지역별 인구 수의 합을 float형으로 저장함
sum_covid  = float(sum(n_covid)) # TODO: The total number of new cases
            # 변수 sum_covid에 지역별 확진자수의 합을 floa형으로 저장함
norm_covid = normalize_data(n_covid, n_people, 1000000) # The new cases per 1 million people

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = (pop / sum_people) * 100 # TODO: The ratio of new cases to the total
    # 지역별 인구 비율 = (지역 인구수 / 총 인구수) * 100
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))
print('')

# TODO: Print COVID-19 new cases by region
print('----------------------------------------------------\n')
print('### Korean COVID-19 New Cases by Region')
print('* Total new cases:', sum_covid)
print('| Region | New Cases | Ratio (%) | New Cases / 1M')
print('| ------ | ---------- | --------- | ------------- |')
for idx, pop in enumerate(n_covid):
    ratio = (pop / sum_covid) * 100
    # 신규 확진비율 = (신규 확진 / 전체 확진) * 100
    print('| %s | %d | %.1f | %.1f |' % (regions[idx], pop, ratio, norm_covid[idx]))
print('')
 
