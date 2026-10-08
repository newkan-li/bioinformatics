# -*- coding: utf-8 -*-
# 统计学习与推理概述及统计学习基础（ch12 p258）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np

# 设置随机种子，保证结果可复现
np.random.seed(42)

# y: (n,) 因变量; X: (n, m) 自变量
n, m = 100, 5
X = np.random.randn(n, m)          # 生成 100x5 的标准正态自变量矩阵
w_true = np.random.randn(m)        # 真实权重向量，长度 5
y = X @ w_true + 0.1 * np.random.randn(n)  # 线性模型 + 小噪声

# 若样本顺序不能变动，则不能随机打乱
# 若可交换，可打乱：
idx = np.random.permutation(n)     # 生成 0..n-1 的随机排列
X_shuffled, y_shuffled = X[idx], y[idx]  # 按同一索引打乱 X 和 y，保持对应关系

print('X.shape =', X.shape)
print('y.shape =', y.shape)
print('X_shuffled.shape =', X_shuffled.shape)
print('y_shuffled.shape =', y_shuffled.shape)
print('前 3 个原始 y:', y[:3])
print('前 3 个打乱后 y:', y_shuffled[:3])

