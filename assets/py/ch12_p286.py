# -*- coding: utf-8 -*-
# LIBSVM子程序与svmtrain选项（ch12 p286）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：scikit-learn, numpy, pandas, matplotlib。安装命令：pip install scikit-learn numpy pandas matplotlib 或 conda install scikit-learn numpy pandas matplotlib

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 加载数据
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 网格搜索寻找最优参数 C 和 gamma（对应 grid.py）
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1],
    'kernel': ['rbf']
}
grid = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy', verbose=1)
grid.fit(X_train_scaled, y_train)

print(f'Best parameters: {grid.best_params_}')
print(f'Best cross-validation score: {grid.best_score_:.4f}')

# 使用最优参数训练最终模型
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test_scaled)
print(f'Test accuracy: {accuracy_score(y_test, y_pred):.4f}')
