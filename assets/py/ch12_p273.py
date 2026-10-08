# -*- coding: utf-8 -*-
# HMM生成观察序列、模型参数与三个基本问题（ch12 p273）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；无需额外依赖（仅用标准库 random）。如需可复现实验可安装 numpy：pip install numpy

import random

# 定义 HMM 参数
states = [0, 1]  # 两个状态
obs_symbols = [0, 1]  # 两个观察符号
pi = [0.6, 0.4]  # 初始状态概率
A = [[0.7, 0.3], [0.4, 0.6]]  # 状态转移矩阵
B = [[0.5, 0.5], [0.1, 0.9]]  # 发射概率矩阵
T = 5  # 序列长度

def sample_from(probs):
    """根据概率分布随机采样一个索引"""
    r = random.random()
    cum = 0.0
    for i, p in enumerate(probs):
        cum += p
        if r < cum:
            return i
    return len(probs) - 1

def generate_hmm(pi, A, B, T):
    """生成状态序列 Q 和观察序列 O"""
    q1 = sample_from(pi)  # 根据 pi 选择初始状态
    O = []
    Q = [q1]
    for t in range(1, T + 1):
        ot = sample_from(B[Q[t - 1]])  # 根据 b_i 选择观察符号
        O.append(ot)
        if t < T:
            qt_next = sample_from(A[Q[t - 1]])  # 根据 A 转移状态
            Q.append(qt_next)
    return Q, O

random.seed(42)  # 固定随机种子以便复现
Q, O = generate_hmm(pi, A, B, T)
print("状态序列 Q:", Q)
print("观察序列 O:", O)

