# -*- coding: utf-8 -*-
# dotplot算法特点与动态规划算法（ch03 p50）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；本段仅用标准库，无需额外安装。可选 numpy 用于矩阵运算：pip install numpy

def needleman_wunsch(s, t, match=2, mismatch=-1, gap=-1):
    m, n = len(s), len(t)
    # 初始化 (m+1) x (n+1) 得分矩阵
    M = [[0]*(n+1) for _ in range(m+1)]
    # 第一列：s 前缀与空序列比对
    for i in range(1, m+1):
        M[i][0] = M[i-1][0] + gap
    # 第一行：t 前缀与空序列比对
    for j in range(1, n+1):
        M[0][j] = M[0][j-1] + gap
    # 填表
    for i in range(1, m+1):
        for j in range(1, n+1):
            score = match if s[i-1] == t[j-1] else mismatch
            M[i][j] = max(
                M[i-1][j-1] + score,  # 对角线：匹配/错配
                M[i-1][j] + gap,      # 上方：s 中插入空位
                M[i][j-1] + gap       # 左方：t 中插入空位
            )
    return M[m][n]

# 时间复杂度: O(m*n)，空间复杂度: O(m*n)
print(needleman_wunsch("acgctg", "catgt"))

# Smith-Waterman 局部比对核心差异：
# M[i][j] = max(0, M[i-1][j-1]+score, M[i-1][j]+gap, M[i][j-1]+gap)
# 最终得分取矩阵中的最大值
