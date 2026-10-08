# -*- coding: utf-8 -*-
# 聚类分析概述与数据变换（ch12 p265）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   pip install numpy scikit-learn
#   (用到 numpy、sklearn.preprocessing.StandardScaler、sklearn.cluster.KMeans、AgglomerativeClustering)

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

# 原始数据：两列量纲差异很大
X = np.array([[1.0, 200.0],
              [1.2, 210.0],
              [5.0, 100.0],
              [5.2, 105.0]])

# Z-score 标准化：每列减均值除标准差
Xs = StandardScaler().fit_transform(X)
print('Xs =\n', Xs)

# K-means：需预先指定类数 k
km = KMeans(n_clusters=2, random_state=0, n_init=10).fit(Xs)
print('KMeans labels =', km.labels_)

# 层次聚类：不预先指定类数，用距离阈值切树
hc = AgglomerativeClustering(n_clusters=None, distance_threshold=1.5).fit(Xs)
print('Hierarchical labels =', hc.labels_)

# 时间复杂度：K-means 约 O(n*k*p*t)，层次聚类常见 O(n^3) 或 O(n^2 log n)
