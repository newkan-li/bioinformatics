# -*- coding: utf-8 -*-
# Fisher两类线性判别函数推导（ch12 p269）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np

# A 组、B 组样本，每行一个样本，每列一个判别指标
A = np.array([[1.0, 2.0],
              [1.5, 1.8],
              [1.2, 2.2]])
B = np.array([[4.0, 5.0],
              [4.5, 4.8],
              [3.8, 5.2]])

# 计算两组均值向量
muA = A.mean(axis=0)
muB = B.mean(axis=0)

# 组内离差阵 SA、SB，并求和得到 Sw
SA = ((A - muA).T @ (A - muA))
SB = ((B - muB).T @ (B - muB))
Sw = SA + SB

# Fisher 判别系数 c = Sw^{-1}(muA - muB)
c = np.linalg.solve(Sw, muA - muB)
print(c)

# 判别得分
yA = A @ c
yB = B @ c
print(yA.mean(), yB.mean())

# 时间复杂度：O(n*p^2 + p^3)
