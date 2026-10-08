# -*- coding: utf-8 -*-
# MATLAB序列分析：互补链、二聚体、密码子与ORF（ch12 p289）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, matplotlib。安装命令：pip install biopython matplotlib 或 conda install -c conda-forge biopython matplotlib

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt
from collections import Counter

seq_str = 'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'
seq = Seq(seq_str)

# 1. 反向互补
rc = seq.reverse_complement()
print("反向互补:", rc)

# 2. 二聚体计数并绘制柱状图
dimers = [seq_str[i:i+2] for i in range(len(seq_str)-1)]
dimer_counts = Counter(dimers)
print("二聚体计数:", dict(dimer_counts))

plt.figure(figsize=(10,4))
plt.bar(dimer_counts.keys(), dimer_counts.values())
plt.title("Dimer Counts")
plt.xlabel("Dimer")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("dimer_counts.png")
plt.show()

# 3. 密码子使用计数
codons = [seq_str[i:i+3] for i in range(0, len(seq_str)-2, 3)]
codon_counts = Counter(codons)
print("密码子计数:", dict(codon_counts))

# 4. 指定阅读框（Frame=1，即从第0位开始）
codons_frame1 = [seq_str[i:i+3] for i in range(0, len(seq_str)-2, 3)]
print("Frame 1 密码子:", codons_frame1)

# 5. 查找 ORF（简化版：查找起始密码子 ATG 到终止密码子）
start_codons = ['ATG']
stop_codons = ['TAA', 'TAG', 'TGA']
orf_list = []
for frame in range(3):
    for i in range(frame, len(seq_str)-2, 3):
        codon = seq_str[i:i+3]
        if codon in start_codons:
            for j in range(i+3, len(seq_str)-2, 3):
                stop = seq_str[j:j+3]
                if stop in stop_codons:
                    orf_list.append((frame+1, i+1, j+3, seq_str[i:j+3]))
                    break
print("ORFs:", orf_list)
