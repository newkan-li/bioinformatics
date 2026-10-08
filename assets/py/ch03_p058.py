# -*- coding: utf-8 -*-
# ClustalX 结果界面与 MultAlin 多序列比对工具（ch03 p58）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython。安装命令：pip install biopython 或 conda install -c conda-forge biopython。若需调用外部 Clustal 程序，请确保系统已安装 clustalw/clustalo（Linux: sudo apt-get install clustalw clustalo；macOS: brew install clustal-w clustal-omega）。

import subprocess
import os
from Bio import AlignIO

# 1. 定义输入输出文件
input_fasta = "input.fasta"
output_aln = "output.aln"

# 2. 调用 Clustal Omega 进行多序列比对
# 注意：--force 覆盖已有输出文件
cmd = [
    "clustalo",
    "-i", input_fasta,
    "-o", output_aln,
    "--outfmt=clustal",
    "--force"
]
print("运行命令:", " ".join(cmd))
subprocess.run(cmd, check=True)

# 3. 读取比对结果并打印基本信息
alignment = AlignIO.read(output_aln, "clustal")
print(f"比对序列数: {len(alignment)}")
print(f"比对长度: {alignment.get_alignment_length()}")
print("前两条序列的前 60 个字符:")
for record in alignment[:2]:
    print(f"{record.id}: {str(record.seq)[:60]}...")

# 4. 批量比对示例：遍历当前目录下所有 .fasta 文件
for fname in os.listdir("."):
    if fname.endswith(".fasta"):
        out_name = fname.replace(".fasta", ".aln")
        batch_cmd = [
            "clustalo",
            "-i", fname,
            "-o", out_name,
            "--outfmt=clustal",
            "--force"
        ]
        print(f"批量比对: {fname} -> {out_name}")
        subprocess.run(batch_cmd, check=True)

