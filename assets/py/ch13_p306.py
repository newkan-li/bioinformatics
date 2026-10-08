# -*- coding: utf-8 -*-
# BioPerl SeqIO 读写与序列对象获取（ch13 p306）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：biopython。安装：pip install biopython 或 conda install -c conda-forge biopython。

from Bio import SeqIO
from Bio import Entrez

# 方法一：格式转换 GenBank -> FASTA
# 假设已有 input.gb 文件；若无，可用 Entrez 下载
# 这里演示从本地文件读取并写出 FASTA

# 创建示例 GenBank 文件（若不存在）
import os
if not os.path.exists('input.gb'):
    with open('input.gb', 'w') as f:
        f.write('LOCUS       TEST0001        12 bp    DNA     linear   UNC 01-JAN-2000\n')
        f.write('DEFINITION  Test sequence.\n')
        f.write('ACCESSION   TEST0001\n')
        f.write('VERSION     TEST0001.1\n')
        f.write('FEATURES             Location/Qualifiers\n')
        f.write('     source          1..12\n')
        f.write('                     /organism=\"synthetic\"\n')
        f.write('ORIGIN\n')
        f.write('        1 atgcatgcat gc\n')
        f.write('//\n')

# 1. 格式转换
with open('input.gb') as in_handle, open('output.fasta', 'w') as out_handle:
    for record in SeqIO.parse(in_handle, 'genbank'):
        SeqIO.write(record, out_handle, 'fasta')
print('转换完成，输出 output.fasta')

# 2. 获取 sequence 对象
# 2.1 从文件读取
print('--- 从文件读取 ---')
for record in SeqIO.parse('input.gb', 'genbank'):
    print(record.id, '\t', record.seq)

# 2.2 从 NCBI 下载（需要网络）
Entrez.email = 'your_email@example.com'  # 必须设置邮箱
try:
    handle = Entrez.efetch(db='nucleotide', id='AB000425', rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()
    print('--- GenBank 下载 ---')
    print(record.description)
except Exception as e:
    print('网络下载失败（可能无网络）:', e)

# 2.3 从 NCBI 下载蛋白序列
try:
    handle = Entrez.efetch(db='protein', id='NP_000546', rettype='fasta', retmode='text')
    record = SeqIO.read(handle, 'fasta')
    handle.close()
    print('--- GenPept 下载 ---')
    print(record.seq)
except Exception as e:
    print('网络下载失败（可能无网络）:', e)

