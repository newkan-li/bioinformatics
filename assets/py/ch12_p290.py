# -*- coding: utf-8 -*-
# MATLAB系统发育树构建与基因芯片数据分析函数（ch12 p290）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, matplotlib。安装命令：pip install biopython matplotlib 或 conda install -c conda-forge biopython matplotlib

from Bio import Entrez, SeqIO, AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo import draw
import matplotlib.pyplot as plt

Entrez.email = "student@example.com"

data = [
    ('Mountain Gorilla Rwanda', 'AF089820'),
    ('Chimp Troglodytes', 'AF176766')
]

# 1. 获取序列
seqs = []
for name, acc in data:
    with Entrez.efetch(db="nucleotide", id=acc, rettype="fasta", retmode="text") as handle:
        record = SeqIO.read(handle, "fasta")
        record.id = name
        record.description = name
        seqs.append(record)

# 2. 多序列比对（这里使用 ClustalW 需要外部程序，改用 Bio.Align.PairwiseAligner 或简单对齐）
# 为简化，假设序列已比对，直接构建 MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

aligned_seqs = []
for rec in seqs:
    aligned_seqs.append(SeqRecord(rec.seq, id=rec.id, description=rec.description))

alignment = MultipleSeqAlignment(aligned_seqs)

# 3. 计算距离矩阵
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)
print("距离矩阵:")
print(dm)

# 4. 构建 UPGMA 树
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)
print("树结构:")
print(tree)

# 5. 可视化
draw(tree, do_show=False)
plt.savefig("phylogenetic_tree.png")
plt.show()
