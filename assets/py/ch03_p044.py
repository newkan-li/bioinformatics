# -*- coding: utf-8 -*-
# 序列比对打分目的与打分矩阵概念（ch03 p44）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+
#   无需额外依赖（仅使用标准库）
#   可选：pip install biopython

# p44: 序列比对打分目的与打分矩阵概念

# 简单代价模型：相同得 1，不同得 -1
def simple_score(a, b):
    return 1 if a == b else -1

# 矩阵打分模型：从预先定义的矩阵中查表得分
def matrix_score(a, b, matrix):
    return matrix[a][b]

# 一个极简的 BLOSUM62 子集（仅包含 A 和 G）
blosum62_mini = {
    "A": {"A": 4, "G": 0},
    "G": {"A": 0, "G": 6},
}

# 简单模型下 A vs G 得 -1
print(simple_score("A", "G"))
# 矩阵模型下 A vs G 得 0
print(matrix_score("A", "G", blosum62_mini))

