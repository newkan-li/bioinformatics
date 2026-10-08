# -*- coding: utf-8 -*-
# BioPerl 模块分类与功能概览（ch13 p308）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython。安装命令：pip install biopython 或 conda install -c conda-forge biopython

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio.Restriction import Analysis, RestrictionBatch, CommOnly
from collections import Counter

# 示例：统计碱基组成（对应 Bio::Tools::SeqStats->count_monomers）
seq_str = 'ATGCGTACGTAGCTAGCTAG'
seq = Seq(seq_str)
counts = Counter(str(seq))
for base in sorted(counts):
    print(f"{base}: {counts[base]}")

# 示例：限制性酶切分析（对应 Bio::Restriction::Analysis）
rb = RestrictionBatch(CommOnly)
analysis = Analysis(rb, seq)
for enzyme in analysis.full():
    sites = analysis.full()[enzyme]
    print(f"{enzyme} sites: {len(sites)}")

# 示例：远程 BLAST 提交（对应 Bio::Tools::Run::RemoteBlast）
# 注意：需要联网，且 NCBI 可能限制频率；此处仅演示代码结构
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

# 假设 query.fasta 存在，内容为一条蛋白序列
# 实际运行时请确保文件存在
# with open('query.fasta') as f:
#     query_seq = f.read()
# result_handle = NCBIWWW.qblast('blastp', 'swissprot', query_seq, expect=1e-10)
# blast_records = NCBIXML.parse(result_handle)
# for record in blast_records:
#     for alignment in record.alignments:
#         for hsp in alignment.hsps:
#             print(alignment.title, '\t', hsp.score)

# 时间复杂度：取决于具体模块与数据规模
