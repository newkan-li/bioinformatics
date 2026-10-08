# -*- coding: utf-8 -*-
# DNA打分矩阵与氨基酸打分矩阵（ch03 p45）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+
#   依赖：numpy, biopython
#   安装命令：
#   pip install numpy biopython
#   或 conda install numpy biopython

# p45: DNA打分矩阵与氨基酸打分矩阵
import numpy as np

# DNA 碱基顺序
bases = ["A", "G", "C", "T"]

# DNA 打分矩阵（示例：转换/颠换差异）
# 对角线为相同碱基得分，非对角线为不同碱基得分
dna_matrix = np.array([
    [0.99, 0.006, 0.002, 0.002],
    [0.006, 0.99, 0.002, 0.002],
    [0.002, 0.002, 0.99, 0.006],
    [0.002, 0.002, 0.006, 0.99],
])

def dna_score(x, y):
    """根据碱基字符返回 DNA 打分矩阵中的值。"""
    return dna_matrix[bases.index(x)][bases.index(y)]

# A vs G：转换（嘌呤之间），得分 0.006
print(dna_score("A", "G"))
# A vs C：颠换（嘌呤 vs 嘧啶），得分 0.002
print(dna_score("A", "C"))

# 氨基酸打分矩阵：使用 Biopython 加载 BLOSUM62
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")
# A vs G 在 BLOSUM62 中的得分
print(blosum62["A"]["G"])

