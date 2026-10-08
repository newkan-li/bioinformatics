# -*- coding: utf-8 -*-
# 最大似然估计与对数似然函数（ch12 p264）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   pip install numpy
#   (仅用标准库 math 与 numpy，无需 biopython)

from math import log
import numpy as np

# ===== 多项分布 MLE =====
counts = [12, 24, 14]          # 红、白、黑三类计数
n = sum(counts)                # 总样本数

# 对数似然函数（忽略与 p 无关的常数项）
def loglik(p):
    return sum(c * log(pi) for c, pi in zip(counts, p))

# 约束 sum(p)=1 下，MLE 就是频率
p_hat = [c / n for c in counts]
print('p_hat =', p_hat)
print('loglik(p_hat) =', loglik(p_hat))

# ===== 正态样本 MLE =====
y = np.array([1.2, 2.3, 1.8, 2.1])
mu_hat = y.mean()                              # 均值 MLE
sigma2_hat = ((y - mu_hat) ** 2).mean()        # 方差 MLE（除以 n，不是 n-1）
print('mu_hat =', mu_hat)
print('sigma2_hat =', sigma2_hat)

# 时间复杂度：O(n)，n 为样本数/类别计数总数
