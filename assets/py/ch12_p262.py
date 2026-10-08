# -*- coding: utf-8 -*-
# 统计学习理论总结、支持向量机与基于概率的方法；参数估计量的评选标准（ch12 p262）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：scikit-learn, numpy。安装命令：pip install scikit-learn numpy 或 conda install scikit-learn numpy

from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np

# 生成随机数据：4 个特征，标签由前两个特征之和是否大于 0 决定
X = np.random.randn(200, 4)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 划分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 支持向量机（RBF 核）
clf_svm = svm.SVC(kernel='rbf', C=1.0, gamma='scale')
clf_svm.fit(X_train, y_train)
print('SVM accuracy:', clf_svm.score(X_test, y_test))

# 朴素贝叶斯（基于概率的方法）
clf_nb = GaussianNB()
clf_nb.fit(X_train, y_train)
print('NB accuracy:', clf_nb.score(X_test, y_test))
