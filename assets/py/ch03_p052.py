# -*- coding: utf-8 -*-
# BLAST算法原理与特点（ch03 p52）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（仅标准库）。如需可选加速可安装：pip install biopython

from dataclasses import dataclass
from typing import List

@dataclass
class Hit:
    score: int
    db_id: str
    db_start: int
    db_end: int
    query_start: int
    query_end: int

def make_words(seq: str, k: int) -> set:
    # 生成所有长度为 k 的词（k-mer）
    return {seq[i:i+k] for i in range(len(seq) - k + 1)}

def find_all(seq: str, word: str) -> List[int]:
    # 返回 word 在 seq 中所有出现的起始位置
    positions = []
    start = 0
    while True:
        idx = seq.find(word, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1
    return positions

def extend(db_seq: str, db_pos: int, query: str, word: str, T: int, X: int) -> Hit:
    # 简化版延伸：以命中词为中心，向左右逐位比较，匹配 +1，错配 -X
    score = len(word)
    # 向左延伸
    i = db_pos - 1
    j = query.find(word) - 1
    while i >= 0 and j >= 0:
        if db_seq[i] == query[j]:
            score += 1
        else:
            score -= X
            if score < T:
                break
        i -= 1
        j -= 1
    # 向右延伸
    i = db_pos + len(word)
    j = query.find(word) + len(word)
    while i < len(db_seq) and j < len(query):
        if db_seq[i] == query[j]:
            score += 1
        else:
            score -= X
            if score < T:
                break
        i += 1
        j += 1
    return Hit(score=score, db_id="db", db_start=db_pos, db_end=i, query_start=j, query_end=j)

def blast(query: str, db: List[str], word_len: int = 3, T: int = 11, X: int = 1) -> List[Hit]:
    words = make_words(query, word_len)  # 1) 编译查询序列生成词列表
    hits = []
    for rec in db:                        # 2) 扫描数据库
        for w in words:
            for pos in find_all(rec, w):
                hit = extend(rec, pos, query, w, T, X)  # 3) 向两端延伸
                if hit.score >= T:
                    hits.append(hit)
    return sorted(hits, key=lambda h: -h.score)

if __name__ == "__main__":
    query = "ACGTACGT"
    db = ["TTACGTAA"]
    hits = blast(query, db, word_len=3, T=4, X=1)
    for h in hits:
        print(h)

