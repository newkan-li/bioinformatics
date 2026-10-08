# -*- coding: utf-8 -*-
# 不同打分矩阵的双序列比对示例（ch03 p48）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   pip install biopython
#   （Biopython 自带 PAM250、BLOSUM62 等替换矩阵）

from Bio import Align
from Bio.Align import substitution_matrices

seq1 = "HEAGAWGHEE"
seq2 = "PAWHEAE"

for matrix_name in ["PAM250", "BLOSUM62"]:
    matrix = substitution_matrices.load(matrix_name)  # 加载打分矩阵
    aligner = Align.PairwiseAligner()                  # 创建比对器
    aligner.substitution_matrix = matrix               # 设置替换矩阵
    aligner.open_gap_score = -10                       # 开gap罚分
    aligner.extend_gap_score = -0.5                    # 延伸gap罚分
    alignments = aligner.align(seq1, seq2)             # 执行比对
    best = alignments[0]                               # 取最优比对
    print(f"--- {matrix_name} ---")
    print(best)
    print("Score:", best.score)

