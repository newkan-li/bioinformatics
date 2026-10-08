# -*- coding: utf-8 -*-
# 常用距离与相似系数（ch12 p266）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   pip install numpy scipy
#   (用到 numpy、scipy.spatial.distance.mahalanobis、cosine)

import numpy as np
from scipy.spatial.distance import mahalanobis, cosine

X = np.array([[1.0, 2.0],
              [2.0, 1.0],
              [5.0, 5.0]])

# 欧氏距离矩阵：利用广播一次性算两两距离
D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2))
print('Euclidean distance matrix:\n', D)

# 马氏距离：考虑协方差结构
S = np.cov(X.T)                 # 协方差矩阵
S_inv = np.linalg.inv(S)        # 逆矩阵
d_m = mahalanobis(X[0], X[1], S_inv)
print('Mahalanobis d(0,1) =', d_m)

# 兰氏距离：要求所有分量 > 0
def lance_williams(a, b):
    return np.sum(np.abs(a - b) / (a + b))
print('Lance-Williams d(0,1) =', lance_williams(X[0], X[1]))

# 夹角余弦：1 - cosine 即余弦距离
print('Cosine distance d(0,1) =', 1 - cosine(X[0], X[1]))

# 时间复杂度：两两距离 O(n^2*p)
