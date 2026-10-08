# -*- coding: utf-8 -*-
# 经验非线性方法与过拟合问题（ch12 p260）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy, scikit-learn。安装命令：pip install numpy scikit-learn 或 conda install numpy scikit-learn

import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 构造非线性回归数据：y = sin(x0) + x1^2 + 噪声
X = np.random.randn(200, 5)
y = np.sin(X[:, 0]) + X[:, 1] ** 2 + 0.1 * np.random.randn(200)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# 黑箱式学习：调整内部节点连接权重
ann = MLPRegressor(
    hidden_layer_sizes=(10, 10),   # 两个隐藏层，每层 10 个神经元
    activation='relu',             # 激活函数 ReLU
    solver='adam',                 # 优化器 Adam
    max_iter=2000,                 # 最大迭代次数
    random_state=0                 # 随机种子
)
ann.fit(X_train, y_train)          # 训练模型

print('train R^2:', ann.score(X_train, y_train))
print('test  R^2:', ann.score(X_test, y_test))

