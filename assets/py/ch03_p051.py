# -*- coding: utf-8 -*-
# 动态规划算法计算示例（ch03 p51）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；本段仅用标准库，无需额外安装。可选 numpy 用于矩阵展示：pip install numpy

s = "acgctg"
t = "catgt"
match, mismatch, gap = 2, -1, -1

def dp_global(s, t):
    m, n = len(s), len(t)
    # 初始化 (m+1) x (n+1) 矩阵
    M = [[0]*(n+1) for _ in range(m+1)]
    # 第一列
    for i in range(1, m+1):
        M[i][0] = M[i-1][0] + gap
    # 第一行
    for j in range(1, n+1):
        M[0][j] = M[0][j-1] + gap
    # 填表
    for i in range(1, m+1):
        for j in range(1, n+1):
            d = match if s[i-1] == t[j-1] else mismatch
            M[i][j] = max(M[i-1][j-1]+d, M[i-1][j]+gap, M[i][j-1]+gap)
    return M

M = dp_global(s, t)
for row in M:
    print(row)
print("全局比对得分:", M[len(s)][len(t)])

# 时间复杂度: O(m*n)
# 示例 M[1][1] = max(0+(-1), -1+(-1), -1+(-1)) = -1
