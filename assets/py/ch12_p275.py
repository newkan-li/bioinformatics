# -*- coding: utf-8 -*-
# 前向算法计算示例与后向算法定义（ch12 p275）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；无需额外依赖（仅用标准库）。

# 后向算法（Backward Algorithm）
# 输入：O, A, B, pi, N, T
# 输出：P(O|lambda)

# 示例参数（与 p274 一致，但用索引表示）
N = 3  # 状态数
T = 3  # 观察序列长度
O = [0, 2, 3]  # 观察索引：Dry=0, Dryish=1, Damp=2, Soggy=3

A = [
    [0.500, 0.250, 0.250],
    [0.375, 0.250, 0.375],
    [0.125, 0.625, 0.250]
]

B = [
    [0.60, 0.20, 0.15, 0.05],
    [0.25, 0.25, 0.25, 0.25],
    [0.05, 0.10, 0.35, 0.50]
]

pi = [0.63, 0.17, 0.20]

# 初始化 beta 矩阵
beta = [[0.0] * N for _ in range(T)]

# 1. 初始化
for i in range(N):
    beta[T-1][i] = 1.0

# 2. 递推
for t in range(T-2, -1, -1):
    for i in range(N):
        beta[t][i] = sum(
            A[i][j] * B[j][O[t+1]] * beta[t+1][j]
            for j in range(N)
        )

# 3. 终止
P_O = sum(pi[i] * B[i][O[0]] * beta[0][i] for i in range(N))
print(P_O)

