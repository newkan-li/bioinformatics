# -*- coding: utf-8 -*-
# Viterbi算法递推计算示例（ch12 p277）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（纯标准库）。如需数值计算可选：pip install numpy

import math

states = ['Sunny','Cloudy','Rainy']
obs    = ['Dry','Dryish','Soggy']

A = [[0.5,0.25,0.25],
     [0.375,0.125,0.5],
     [0.125,0.675,0.2]]
B = [[0.6,0.2,0.2],
     [0.25,0.25,0.5],
     [0.05,0.1,0.85]]
pi = [0.63,0.17,0.20]
O  = [0,0,2]   # Dry, Dry, Soggy

N, T = len(states), len(O)
delta = [[0.0]*N for _ in range(T)]
psi   = [[0]*N for _ in range(T)]

for i in range(N):
    delta[0][i] = pi[i]*B[i][O[0]]

for t in range(1,T):
    for j in range(N):
        best, arg = -1, 0
        for i in range(N):
            p = delta[t-1][i]*A[i][j]
            if p > best: best, arg = p, i
        delta[t][j] = best*B[j][O[t]]
        psi[t][j]   = arg
    print('Day', t+1, 'delta=', delta[t], 'psi=', psi[t])

# 预期第3天数值：
# Sunny  ~ 7.088e-4  (来自 Sunny)
# Cloudy ~ 5.581e-3  (来自 Rainy)
# Rainy  ~ ...
