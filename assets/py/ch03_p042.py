# -*- coding: utf-8 -*-
# 全局比对与局部比对递归算法（ch03 p42）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外安装包

def global_align(a, b, match=1, mismatch=-1, gap=-2):
    m, n = len(a), len(b)
    S = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        S[i][0] = S[i-1][0] + gap
    for j in range(1, n+1):
        S[0][j] = S[0][j-1] + gap
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = S[i-1][j-1] + (match if a[i-1] == b[j-1] else mismatch)
            up = S[i-1][j] + gap
            left = S[i][j-1] + gap
            S[i][j] = max(diag, up, left)
    return S[m][n]

print(global_align("ACGGTT", "ACGTT"))
