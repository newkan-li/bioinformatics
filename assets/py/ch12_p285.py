# -*- coding: utf-8 -*-
# SVM主要缺点与LIBSVM简介（ch12 p285）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：scikit-learn, numpy, pandas, matplotlib。安装命令：pip install scikit-learn numpy pandas matplotlib 或 conda install scikit-learn numpy pandas matplotlib

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 加载鸢尾花数据集（二分类：取前两类）
iris = datasets.load_iris()
X = iris.data[:100, :2]  # 取前两个特征便于可视化
y = iris.target[:100]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据标准化（对应 svm-scale）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 训练 SVM 模型（对应 svm-train -s 0 -t 2 -c 1 -g 0.1）
# -s 0: C-SVC, -t 2: RBF 核, -c 1: C=1, -g 0.1: gamma=0.1
model = SVC(kernel='rbf', C=1.0, gamma=0.1)
model.fit(X_train_scaled, y_train)

# 预测（对应 svm-predict）
y_pred = model.predict(X_test_scaled)

# 评估
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc:.4f}')
print(classification_report(y_test, y_pred))

# 可视化决策边界
x_min, x_max = X_train_scaled[:, 0].min() - 1, X_train_scaled[:, 0].max() + 1
y_min, y_max = X_train_scaled[:, 1].min() - 1, X_train_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_train, edgecolors='k')
plt.title('SVM (RBF kernel) Decision Boundary')
plt.xlabel('Feature 1 (scaled)')
plt.ylabel('Feature 2 (scaled)')
plt.show()
