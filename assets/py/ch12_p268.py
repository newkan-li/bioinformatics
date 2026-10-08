# -*- coding: utf-8 -*-
# 主成分分析步骤与Fisher判别引入（ch12 p268）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np

# 原始数据矩阵，每行一个样本，每列一个变量
X = np.array([[2.5, 2.4],
              [0.5, 0.7],
              [2.2, 2.9],
              [1.9, 2.2],
              [3.1, 3.0]])

# 1. 标准化：减去均值，除以样本标准差（ddof=1）
Xc = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)

# 2. 计算样本相关系数矩阵
R = np.corrcoef(Xc, rowvar=False)

# 3. 特征根与特征向量，eigh 返回升序，需降序排列
vals, vecs = np.linalg.eigh(R)
idx = np.argsort(vals)[::-1]
vals, vecs = vals[idx], vecs[:, idx]
print(vals)
print(vecs)

# 4. 选择前 m 个主分量，计算主成分得分
m = 1
scores = Xc @ vecs[:, :m]
print(scores)

# 时间复杂度：O(n*p^2 + p^3)
