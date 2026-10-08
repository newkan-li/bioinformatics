# -*- coding: utf-8 -*-
# 多序列比对概念、应用与算法（ch03 p56）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np
from itertools import product

# 多序列比对动态规划核心思想演示（简化版，仅展示N=2的情况）
# 对于N条序列，DP表是N维的，这里以2条序列为例说明

def pairwise_dp(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """双序列动态规划比对，返回得分矩阵和最优比对"""
    m, n = len(seq1), len(seq2)
    score = np.zeros((m+1, n+1))
    # 初始化边界
    for i in range(1, m+1):
        score[i][0] = score[i-1][0] + gap
    for j in range(1, n+1):
        score[0][j] = score[0][j-1] + gap
    # 填充矩阵
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            up = score[i-1][j] + gap
            left = score[i][j-1] + gap
            score[i][j] = max(diag, up, left)
    # 回溯
    align1, align2 = '', ''
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and score[i][j] == score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif i > 0 and score[i][j] == score[i-1][j] + gap:
            align1 = seq1[i-1] + align1
            align2 = '-' + align2
            i -= 1
        else:
            align1 = '-' + align1
            align2 = seq2[j-1] + align2
            j -= 1
    return score, align1, align2

# 演示双序列比对
seq1 = 'ACGT'
seq2 = 'ACGT'
score, align1, align2 = pairwise_dp(seq1, seq2)
print('Score matrix:')
print(score)
print('Alignment:')
print(align1)
print(align2)

# 说明：对于N条序列，DP表是N维的，转移有2^N-1种，时间复杂度O(2^N * L^N)
# 这里仅演示N=2的情况，N>2时计算量指数增长

