# -*- coding: utf-8 -*-
# ClustalX/W多序列比对工具及操作步骤（ch03 p57）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, numpy, scipy。安装命令：pip install biopython numpy scipy 或 conda install -c conda-forge biopython numpy scipy

from Bio import AlignIO, SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo import draw
import matplotlib.pyplot as plt
import numpy as np

# 模拟 ClustalW 渐进式多序列比对流程
# 注意：真实 ClustalW 是外部程序，这里用 Biopython 演示类似步骤

# 1. 读取序列（模拟加载）
sequences = [
    SeqIO.read('seq1.fa', 'fasta'),
    SeqIO.read('seq2.fa', 'fasta'),
    SeqIO.read('seq3.fa', 'fasta')
]
# 如果没有文件，可以手动创建 SeqRecord 对象
# 这里为了可运行，直接创建示例序列
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seqs = [SeqRecord(Seq('ACGTACGT'), id='seq1'),
        SeqRecord(Seq('ACGTTCGT'), id='seq2'),
        SeqRecord(Seq('ACGTACGA'), id='seq3')]

# 2. 两两比对计算距离矩阵
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(seqs)
print('Distance matrix:')
print(distance_matrix)

# 3. 构建引导树（使用 NJ）
constructor = DistanceTreeConstructor()
tree = constructor.nj(distance_matrix)
print('Guide tree:')
print(tree)

# 4. 按树逐步加入序列进行比对（这里简化为直接输出树）
# 真实 ClustalW 会使用 profile-profile 比对，这里不实现

# 5. 保存比对结果（模拟）
# 实际中会生成比对文件，这里仅打印
print('Alignment completed (simulated).')

