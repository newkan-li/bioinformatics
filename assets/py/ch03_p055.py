# -*- coding: utf-8 -*-
# PSI-BLAST阈值与PHI-BLAST模式识别（ch03 p55）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, numpy。安装命令：pip install biopython numpy 或 conda install -c conda-forge biopython numpy

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import numpy as np
import re

# 1. 模拟 PSI-BLAST 迭代构建 PSSM 的简化流程
# 注意：真实 PSI-BLAST 需要本地 BLAST+ 或 NCBI 在线服务，这里用伪代码逻辑演示

def build_pssm(sequences):
    """根据一组序列构建简单的位置特异性打分矩阵 (PSSM)"""
    # 假设所有序列等长，用简单计数代替真实 PSSM
    length = len(sequences[0])
    pssm = np.zeros((length, 20))  # 20 种氨基酸
    aa_list = 'ACDEFGHIKLMNPQRSTVWY'
    for seq in sequences:
        for i, aa in enumerate(seq):
            if aa in aa_list:
                pssm[i, aa_list.index(aa)] += 1
    # 归一化为频率
    pssm = pssm / pssm.sum(axis=1, keepdims=True)
    return pssm

def search(pssm, database):
    """模拟用 PSSM 搜索数据库，返回带 evalue 的命中"""
    hits = []
    for seq_record in database:
        # 简化打分：随机生成 evalue 模拟
        evalue = np.random.exponential(0.01)
        hits.append({'id': seq_record.id, 'evalue': evalue, 'seq': str(seq_record.seq)})
    return hits

def msa(sequences):
    """模拟多序列比对，这里直接返回序列列表"""
    return sequences

# 模拟查询序列和数据库
query = SeqRecord(Seq('MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP'), id='query')
db = [SeqRecord(Seq('MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP'), id='seq1'),
      SeqRecord(Seq('MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP'), id='seq2'),
      SeqRecord(Seq('MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP'), id='seq3')]

# PSI-BLAST 迭代
num_iterations = 3
threshold = 0.005
pssm = build_pssm([str(query.seq)])
for it in range(num_iterations):
    hits = search(pssm, db)
    sel = [h for h in hits if h['evalue'] < threshold]
    print(f'Iteration {it+1}: selected {len(sel)} hits')
    if sel:
        pssm = build_pssm([h['seq'] for h in sel])
    else:
        break

# 2. PHI-BLAST 模式匹配示例
pattern = r'[LIV]-{KRP}-x(2)-[ST]'  # 模式：LIV中任一个，非KRP，任意两个，ST中任一个
# 将模式转换为正则表达式
regex_pattern = r'[LIV][^KRP]..[ST]'
for seq_record in db:
    seq_str = str(seq_record.seq)
    matches = re.finditer(regex_pattern, seq_str)
    for match in matches:
        print(f'PHI-BLAST pattern found in {seq_record.id} at position {match.start()}: {match.group()}')

