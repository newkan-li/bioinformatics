# -*- coding: utf-8 -*-
# HMM解码问题与Viterbi算法（ch12 p276）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（纯标准库）。如需数值计算可选：pip install numpy

def viterbi(A, B, pi, O):
    N = len(A)          # 状态数
    T = len(O)          # 观测序列长度
    delta = [[0.0]*N for _ in range(T)]  # delta[t][i]: 到 t 时刻以状态 i 结尾的最优路径概率
    psi   = [[0]*N for _ in range(T)]    # psi[t][i]: 该最优路径在 t-1 时刻的状态

    # 初始化
    for i in range(N):
        delta[0][i] = pi[i] * B[i][O[0]]
        psi[0][i] = 0

    # 递推
    for t in range(1, T):
        for j in range(N):
            best, arg = -1.0, 0
            for i in range(N):
                p = delta[t-1][i] * A[i][j]
                if p > best:
                    best, arg = p, i
            delta[t][j] = best * B[j][O[t]]
            psi[t][j]   = arg

    # 终止
    best, qT = -1.0, 0
    for i in range(N):
        if delta[T-1][i] > best:
            best, qT = delta[T-1][i], i

    # 回溯
    Q = [0]*T
    Q[T-1] = qT
    for t in range(T-2, -1, -1):
        Q[t] = psi[t+1][Q[t+1]]
    return Q, best

# 时间复杂度: O(T * N^2)
# 最小示例
A = [[0.7,0.3],[0.4,0.6]]
B = [[0.5,0.5],[0.1,0.9]]
pi = [0.6,0.4]
O = [0,1,0]
print(viterbi(A,B,pi,O))
