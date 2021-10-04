# -*- coding: utf-8 -*-
import statistics

# 데이터를 읽어오는 함수
def read_data(filename):
    data = []
    # TODO
    with open(filename, 'r') as f:
        for line in f:  # 각 행을 리스트로 만듦
            values =  []   # 값을 담을 리스트
            if line.startswith('#'):
                continue
            for word in line.split(','):    # ,을 기준으로 점수를 분류해서
                values.append(int(word))    # 리스트에 저장
            data.append(values)
    return data

# 데이터의 평균을 계산하는 부분
def add_weighted_average(data, weight):
    for row in data:
        average = weight[0] * row[0] + weight[1] * row[1]
        row.append(average)

def analyze_data(data):     # 데이터를 분석하는 부분
    mean = sum(data) / len(data)
    squares = map(lambda x: x**2, data)
    var = sum(squares) / len(data) - mean**2
    median = statistics.median(data)
    return mean, var, median, min(data), max(data)  # 분석 결과 return

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')     # 2차원 리스트로 이루어진 data
    if data and len(data[0]) == 2:  # 행의 개수가 2개라면 잘 읽어온 것
        print('### Individual Score')   # 개인별 합산 점수
        add_weighted_average(data, [40/125, 60/100])    # 전체 평균을 data에 추가 시켜줌
        if len(data[0]) == 3:   # 행의 개수가 3개가 되면 잘 읽어온 것
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')    # 행으로 바꾸어 출력
            print()

            print('### Examination Analysis')   # 점수 분석
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]   # list comprehension (c를 0부터 2까지 -> 2차원 리스트 만듦 => 각 시험당으로 출력하기 위함!!)
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')
