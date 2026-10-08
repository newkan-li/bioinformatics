# -*- coding: utf-8 -*-
# 最小二乘估计与最大似然估计（ch12 p263）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy, scipy。安装命令：pip install numpy scipy 或 conda install numpy scipy

import numpy as np
from scipy.optimize import minimize

# 最小二乘估计总体均值 mu
y = np.array([2.1, 1.9, 2.5, 2.0, 1.8])
mu_ls = np.mean(y)
print('LS mean:', mu_ls)

# 最大似然估计（正态分布均值和方差）
def neg_log_likelihood(params, y):
    mu, sigma = params
    if sigma <= 0:
        return np.inf
    n = len(y)
    return 0.5 * n * np.log(2 * np.pi * sigma ** 2) + np.sum((y - mu) ** 2) / (2 * sigma ** 2)

# 用 Nelder-Mead 数值优化求 MLE
res = minimize(neg_log_likelihood, x0=[0, 1], args=(y,), method='Nelder-Mead')
print('MLE mu, sigma:', res.x)
