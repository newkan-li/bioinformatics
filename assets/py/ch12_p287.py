# -*- coding: utf-8 -*-
# LIBSVM使用示例与MATLAB应用实例引入（ch12 p287）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：scikit-learn, numpy, pandas, matplotlib。安装命令：pip install scikit-learn numpy pandas matplotlib 或 conda install scikit-learn numpy pandas matplotlib

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# 1) 加载数据并划分
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2) 训练集标准化，并保存 scaler（对应 svmscale -s range）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 3) 测试集使用相同的 scaler 标准化（对应 svmscale -r range）
X_test_scaled = scaler.transform(X_test)

# 4) 网格搜索寻找最优参数 C 和 g（对应 grid.py）
param_grid = {'C': [0.1, 1, 10], 'gamma': [0.01, 0.1, 1], 'kernel': ['rbf']}
grid = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train_scaled, y_train)
best_C = grid.best_params_['C']
best_g = grid.best_params_['gamma']
print(f'Best C: {best_C}, Best gamma: {best_g}')

# 5) 使用最优参数训练模型（对应 svmtrain）
model = SVC(kernel='rbf', C=best_C, gamma=best_g)
model.fit(X_train_scaled, y_train)

# 6) 预测（对应 svmpredict）
y_pred = model.predict(X_test_scaled)
print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
print(classification_report(y_test, y_pred))
