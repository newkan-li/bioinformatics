# -*- coding: utf-8 -*-
# 仿射空位罚分与dotplot算法（ch03 p49）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；本段仅用标准库，无需额外安装。如需矩阵可视化可选装 numpy/matplotlib：pip install numpy matplotlib

def affine_gap_penalty(k, a=-4, b=-3):
    # k: 空位长度; a: 起始罚分; b: 延伸罚分
    return a + b * k

# 时间复杂度: O(1)
# 示例: 长度 5 的空位
print(affine_gap_penalty(5))  # -4 + (-3)*5 = -19

# dotplot 算法核心步骤（伪代码）
# 1. 构建 m x n 矩阵，m=|s|, n=|t|
# 2. 若 s[i] == t[j]，则 M[i][j] = 1，否则为 0
# 3. 在矩阵中寻找对角线连续片段
# 时间复杂度: O(m*n)

def dotplot(s, t):
    m, n = len(s), len(t)
    M = [[1 if s[i] == t[j] else 0 for j in range(n)] for i in range(m)]
    return M

print(dotplot("ACGT", "ACGT"))
