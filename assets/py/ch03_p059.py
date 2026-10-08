# -*- coding: utf-8 -*-
# 多序列比对工具练习与本章参考文献（ch03 p59）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython、matplotlib、numpy。安装命令：pip install biopython matplotlib numpy 或 conda install -c conda-forge biopython matplotlib numpy。若需运行 T-Coffee，请确保系统已安装 t_coffee（conda install -c bioconda t-coffee）。

import subprocess
import numpy as np
import matplotlib.pyplot as plt
from Bio import AlignIO

# 1. 准备输入文件 seqs.fasta（假设已存在）
input_fasta = "seqs.fasta"

# 2. 运行 Clustal Omega
cmd_clustal = [
    "clustalo",
    "-i", input_fasta,
    "-o", "aln_clustal.aln",
    "--outfmt=clustal",
    "--force"
]
print("运行 Clustal Omega...")
subprocess.run(cmd_clustal, check=True)

# 3. 运行 T-Coffee（如果已安装）
cmd_tcoffee = [
    "t_coffee",
    input_fasta,
    "-output=clustalw",
    "-outfile=aln_tcoffee.aln"
]
print("运行 T-Coffee...")
try:
    subprocess.run(cmd_tcoffee, check=True)
except FileNotFoundError:
    print("未找到 t_coffee，跳过 T-Coffee 比对。")

# 4. 定义空位统计函数
def gap_stats(path):
    """读取 clustal 格式比对文件，返回序列数、比对长度、总空位数、空位比例。"""
    aln = AlignIO.read(path, "clustal")
    n = len(aln)
    L = aln.get_alignment_length()
    gaps = sum(str(record.seq).count('-') for record in aln)
    return n, L, gaps, gaps / (n * L)

# 5. 比较两种比对结果
for path in ["aln_clustal.aln", "aln_tcoffee.aln"]:
    try:
        n, L, gaps, ratio = gap_stats(path)
        print(f"{path}: 序列数={n}, 长度={L}, 空位数={gaps}, 空位比例={ratio:.4f}")
    except FileNotFoundError:
        print(f"文件 {path} 不存在，跳过。")

# 6. 保守区可视化（空位图）
def plot_gap_map(path, title):
    """绘制空位图：横轴为比对位置，纵轴为序列，黑色表示空位。"""
    aln = AlignIO.read(path, "clustal")
    n = len(aln)
    L = aln.get_alignment_length()
    # 构建矩阵：1 表示空位，0 表示非空位
    matrix = np.zeros((n, L))
    for i, record in enumerate(aln):
        for j, char in enumerate(str(record.seq)):
            if char == '-':
                matrix[i, j] = 1
    plt.figure(figsize=(10, 4))
    plt.imshow(matrix, aspect='auto', cmap='gray_r', interpolation='nearest')
    plt.xlabel("Alignment position")
    plt.ylabel("Sequence index")
    plt.title(title)
    plt.colorbar(label="Gap (1) / Non-gap (0)")
    plt.tight_layout()
    plt.savefig(path.replace('.aln', '_gapmap.png'), dpi=150)
    plt.show()

# 绘制 Clustal 结果的空位图
plot_gap_map("aln_clustal.aln", "Gap map (Clustal Omega)")

