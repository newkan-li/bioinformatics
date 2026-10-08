# -*- coding: utf-8 -*-
# 序列比对的意义与类型概述（ch03 p40）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；安装 Biopython：pip install biopython 或 conda install -c conda-forge biopython

from Bio import pairwise2
from Bio.pairwise2 import format_alignment

seq1 = "ACGGTT"
seq2 = "ACGTT"

# 使用全局比对，匹配得1分，错配和空位不得分也不扣分（globalxx）
for a in pairwise2.align.globalxx(seq1, seq2):
    print(format_alignment(*a))
