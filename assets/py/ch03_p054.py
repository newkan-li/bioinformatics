# -*- coding: utf-8 -*-
# BLAST结果解析与图形化显示（ch03 p54）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 若没有真实 hits.tsv，可先生成一个示例文件
sample = """q1\tdb1\t95.0\t100\t5\t0\t1\t100\t50\t149\t1e-50\t200
q1\tdb2\t80.0\t90\t18\t2\t10\t99\t200\t289\t1e-20\t120
q1\tdb3\t70.0\t80\t24\t3\t20\t99\t300\t379\t1e-10\t80
"""
with open("hits.tsv", "w") as f:
    f.write(sample)

cols = ["qseqid","sseqid","pident","length","mismatch","gapopen",
        "qstart","qend","sstart","send","evalue","bitscore"]
df = pd.read_csv("hits.tsv", sep="\t", names=cols)
print(df)

# 图形化：每条色带表示匹配区域，颜色表示得分高低
fig, ax = plt.subplots(figsize=(10, 4))
for i, row in df.iterrows():
    ax.plot([row.qstart, row.qend], [i, i],
            linewidth=6, color=plt.cm.Reds(row.bitscore / df.bitscore.max()))
ax.set_xlabel("Query position")
ax.set_ylabel("Hit index")
plt.title("BLAST hits on query")
plt.tight_layout()
plt.savefig("blast_hits.png")
plt.show()

# Gap costs: 线性空位罚分，默认 open=11, extend=1
print("Gap costs: open=11, extend=1")

