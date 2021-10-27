import glob, csv
import numpy as np
import matplotlib.pyplot as plt

# 데이터를 읽어오는 부분
def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:     # Construct a file object
            csv_reader = csv.reader(f) # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'): # If 'line' is valid and not a header
                    data.append([int(val) for val in line])      # Append 'line' to 'data' as numbers
            all_data = all_data + data                           # Merge 'data' to 'all_data'
    return all_data

if __name__ == '__main__':
    # Load score data
    scores = np.array(read_data('data/class_score_*.csv'))  # 한국어와 영어 강좌의 데이터를 모두 읽어옴
                                                            # Numpy array로 읽어옴 (접근 용이)
    midtm_range = np.array([0, 125])
    final_range = np.array([0, 100])

    # Estimate a line, final = slope * midterm + y_intercept
    A = np.vstack((scores[:,0], np.ones(len(scores)))).T   # midterm scores
    b = scores[:,1]     # final scores
    line = np.matmul(np.linalg.pinv(A), b)

    # Predict scores
    final = lambda midterm: line[0] * midterm + line[1]
    while True:
        # 중간고사 점수를 입력 받는 부분
        given = float(input('Q) Please input your midterm score (-1: exit)? '))
        if given < 0:   # 음수가 입력되면 종료
            break
        print(f'A) Your final score is expected to {final(given):.3f}.')

    # Plot scores and the estimated line
    plt.figure()
    plt.plot(scores[:,0], scores[:,1], 'r.', label='The given data')
    plt.plot(midtm_range, final(midtm_range), 'b-', label='Prediction')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim(midtm_range)
    plt.ylim(final_range)
    plt.grid()
    plt.legend()
    plt.show()
