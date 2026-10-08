# -*- coding: utf-8 -*-
# 表观遗传修饰测序分析与NGS功能基因组学应用（ch14 p343）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：pysam, biopython, numpy, pandas, matplotlib。安装命令：
#   pip install pysam biopython numpy pandas matplotlib
#   或 conda：
#   conda install -c bioconda pysam biopython numpy pandas matplotlib

import os
import subprocess
import pysam
import numpy as np
import pandas as pd

# 模拟 BS-seq 与 ChIP-seq 流程的 Python 封装
# 注意：真实运行需要 bismark、bowtie2、samtools、macs2 等外部工具

def run_cmd(cmd):
    """执行 shell 命令并打印输出"""
    print(f"[CMD] {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] {result.stderr}")
    else:
        print(f"[OK] {result.stdout[:200]}")
    return result.returncode

# ---------- BS-seq 流程 ----------
# 1. 基因组准备
run_cmd("bismark_genome_preparation --path genome/")

# 2. 双端比对
run_cmd("bismark --genome genome/ -1 bs_r1.fq -2 bs_r2.fq")

# 3. 甲基化提取
run_cmd("bismark_methylation_extractor -s --comprehensive bs.bam")

# 4. 用 pysam 读取 BAM，统计甲基化位点
# 未甲基化 C -> U -> T，甲基化 C 保持 C
def count_methylation(bam_path):
    """统计 BAM 中甲基化/未甲基化 C 的数量"""
    if not os.path.exists(bam_path):
        print(f"[WARN] {bam_path} 不存在，跳过统计")
        return None
    bam = pysam.AlignmentFile(bam_path, "rb")
    methylated = 0
    unmethylated = 0
    for read in bam:
        if read.is_unmapped:
            continue
        seq = read.query_sequence
        if seq is None:
            continue
        for base in seq:
            if base == 'C':
                methylated += 1
            elif base == 'T':
                unmethylated += 1
    bam.close()
    total = methylated + unmethylated
    ratio = methylated / total if total > 0 else 0
    print(f"甲基化 C: {methylated}, 未甲基化 C: {unmethylated}, 比例: {ratio:.3f}")
    return methylated, unmethylated, ratio

count_methylation("bs.bam")

# ---------- ChIP-seq 流程 ----------
# 1. 比对
run_cmd("bowtie2 -x genome_index -U chip.fq -S chip.sam")

# 2. 排序
run_cmd("samtools sort -o chip.bam chip.sam")

# 3. Peak calling
run_cmd("macs2 callpeak -t chip.bam -c input.bam -g hs -n chip_peak")

# 4. 用 pandas 读取 peak 文件
peak_file = "chip_peak_peaks.narrowPeak"
if os.path.exists(peak_file):
    peaks = pd.read_csv(peak_file, sep='\t', header=None,
                        names=['chr','start','end','name','score','strand','fold','pval','qval','summit'])
    print(f"Peak 数量: {len(peaks)}")
    print(peaks.head())
else:
    print(f"[WARN] {peak_file} 不存在，跳过 peak 读取")

# 时间复杂度说明
print("比对 O(N*M)，甲基化提取 O(N)")
