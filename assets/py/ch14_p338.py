# -*- coding: utf-8 -*-
# DNA甲基化测序方法（ch14 p338）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：numpy, biopython。安装命令：
#   pip install numpy biopython

import numpy as np
from Bio import pairwise2
from Bio.Seq import Seq

def bisulfite_align(reads, ref):
    """
    模拟重硫酸盐测序比对：将参考基因组和reads中的C转换为T，然后进行比对。
    reads: list of str, 测序reads
    ref: str, 参考基因组序列
    返回: list of (read, pos) 比对结果，pos为read在参考上的起始位置
    """
    # 将参考基因组中所有C转换为T
    ref_T = ref.replace('C', 'T')
    # 将reads中C转换为T
    reads_T = [r.replace('C', 'T') for r in reads]
    # 使用简单的滑窗比对（实际应用需用Bowtie等）
    alignments = []
    for read in reads_T:
        # 在ref_T中查找read的精确匹配
        pos = ref_T.find(read)
        if pos != -1:
            alignments.append((read, pos))
    return alignments

def methylation_level(alignments, ref):
    """
    计算每个C位点的甲基化比例。
    alignments: list of (read, pos)，read为原始read（未转换），pos为起始位置
    ref: str, 原始参考基因组
    返回: dict, 键为位置，值为甲基化比例
    """
    meth = {}
    for read, pos in alignments:
        for i, base in enumerate(read):
            ref_pos = pos + i
            if ref[ref_pos] == 'C':
                if base == 'C':
                    meth.setdefault(ref_pos, [0, 0])
                    meth[ref_pos][0] += 1  # 甲基化
                elif base == 'T':
                    meth.setdefault(ref_pos, [0, 0])
                    meth[ref_pos][1] += 1  # 未甲基化
    return {p: v[0] / (v[0] + v[1]) for p, v in meth.items()}

if __name__ == '__main__':
    # 示例数据
    ref = 'ACGTACGTACGT'
    reads = ['ACGTACGT', 'ACGTACGT', 'ATGTACGT']  # 第三个read在第二个C处为T
    # 注意：reads中的C在比对前会被转换为T，但甲基化分析使用原始reads
    alignments = bisulfite_align(reads, ref)
    print('Alignments:', alignments)
    meth = methylation_level(alignments, ref)
    print('Methylation levels:', meth)
