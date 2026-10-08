# -*- coding: utf-8 -*-
# 海草湿度HMM示例与穷举法评估（ch12 p274）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；无需额外依赖（仅用标准库 itertools）。

import itertools

# 海草湿度 HMM 示例
states = ['Sunny', 'Cloudy', 'Rainy']
obs = ['Dry', 'Dryish', 'Damp', 'Soggy']

A = {
    'Sunny':  {'Sunny': 0.500, 'Cloudy': 0.250, 'Rainy': 0.250},
    'Cloudy': {'Sunny': 0.375, 'Cloudy': 0.250, 'Rainy': 0.375},
    'Rainy':  {'Sunny': 0.125, 'Cloudy': 0.625, 'Rainy': 0.250}
}

B = {
    'Sunny':  {'Dry': 0.60, 'Dryish': 0.20, 'Damp': 0.15, 'Soggy': 0.05},
    'Cloudy': {'Dry': 0.25, 'Dryish': 0.25, 'Damp': 0.25, 'Soggy': 0.25},
    'Rainy':  {'Dry': 0.05, 'Dryish': 0.10, 'Damp': 0.35, 'Soggy': 0.50}
}

pi = {'Sunny': 0.63, 'Cloudy': 0.17, 'Rainy': 0.20}
O = ['Dry', 'Damp', 'Soggy']

prob = 0.0
for Q in itertools.product(states, repeat=len(O)):
    p = pi[Q[0]] * B[Q[0]][O[0]]
    for t in range(1, len(O)):
        p *= A[Q[t-1]][Q[t]] * B[Q[t]][O[t]]
    prob += p

print(prob)

