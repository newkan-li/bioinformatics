# -*- coding: utf-8 -*-
# MATLAB生物信息工具箱：序列获取与序列分析入门（ch12 p288）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython。安装命令：pip install biopython 或 conda install -c conda-forge biopython

from Bio import Entrez, SeqIO
from Bio.Seq import Seq

# 设置邮箱（NCBI 要求）
Entrez.email = "student@example.com"

acc = "EF221854"

# 1. 获取完整 GenBank 记录并保存到文件
with Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text") as handle:
    record = SeqIO.read(handle, "genbank")
SeqIO.write(record, "EF221854.gb", "genbank")
print("已保存 EF221854.gb")

# 2. 仅获取序列
with Entrez.efetch(db="nucleotide", id=acc, rettype="fasta", retmode="text") as handle:
    seq_record = SeqIO.read(handle, "fasta")
seq = seq_record.seq
print("序列长度:", len(seq))
print("前60个碱基:", seq[:60])

# 3. 获取部分序列（前500个碱基）
seq_partial = seq[:500]
print("部分序列长度:", len(seq_partial))
print("部分序列前60:", seq_partial[:60])
