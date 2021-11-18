# SVM을 이용해 iris 꽃을 분류하는 예시 코드

import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, svm)
from matplotlib.lines import Line2D # For the custom legend

# Load a dataset
iris = datasets.load_iris()

# Train a model
model = svm.SVC() # 모델 생성
model.fit(iris.data, iris.target) # 모델 학습시킴

# Test the model
predict = model.predict(iris.data)  # 모델을 이용해 predict
n_correct = sum(predict == iris.target)

# Visualize testing results
cmap = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]) # cmap == color map
clabel = [Line2D([0], [0], marker='o', lw=0, label=iris.target_names[i], color=cmap[i]) for i in range(len(cmap))]
for (x, y) in [(0, 1), (2, 3)]:
  plt.title(f'svm.SVC ({n_correct}/{len(iris.data)}={n_correct/len(iris.data):.3f})')
  
  plt.scatter(iris.data[:,x], iris.data[:,y], c=cmap[iris.target], edgecolors=cmap[predict])  # 각각의 데이터 출력
  plt.xlabel(iris.feature_names[x])
  plt.ylabel(iris.feature_names[y])
  plt.legend(handles=clabel, framealpha=0.5)
  
  plt.show()
