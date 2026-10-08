# -*- coding: utf-8 -*-
# 支持向量分类决策函数与支持向量回归（ch12 p283）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：numpy。安装命令：
#   pip install numpy
#   或 conda：
#   conda install numpy

import numpy as np

def linear_kernel(a, b):
    """线性核 K(a,b)=a·b"""
    return np.dot(a, b)

def rbf_kernel(a, b, gamma=1.0):
    """RBF 核 K(a,b)=exp(-gamma*||a-b||^2)"""
    diff = a - b
    return np.exp(-gamma * np.dot(diff, diff))

def svm_decision(X_sv, y_sv, alpha, b, x, kernel):
    """
    X_sv: 支持向量, shape=(n_sv, d)
    y_sv: 支持向量标签, shape=(n_sv,)
    alpha: 拉格朗日乘子, shape=(n_sv,)
    b: 偏置
    x: 待预测样本, shape=(d,)
    kernel: 核函数 K(a,b)
    返回：+1 或 -1
    """
    s = 0.0
    for xi, yi, ai in zip(X_sv, y_sv, alpha):
        s += ai * yi * kernel(xi, x)
    return np.sign(s + b)

# 示例：3 个支持向量，2 维特征
X_sv = np.array([[1.0, 2.0],
                 [2.0, 3.0],
                 [-1.0, -1.0]])
y_sv = np.array([1, 1, -1])
alpha = np.array([0.5, 0.8, 0.6])
b = -0.2

x_test = np.array([1.5, 2.5])

pred_linear = svm_decision(X_sv, y_sv, alpha, b, x_test, linear_kernel)
pred_rbf = svm_decision(X_sv, y_sv, alpha, b, x_test, lambda a, b: rbf_kernel(a, b, gamma=0.5))

print('线性核预测:', pred_linear)
print('RBF 核预测:', pred_rbf)

# 时间复杂度：预测 O(n_sv * d)，n_sv 为支持向量数，d 为特征维数

