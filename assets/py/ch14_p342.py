# -*- coding: utf-8 -*-
# 有参考基因组RNA-seq分析策略与ChIP-seq分析（ch14 p342）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, pandas, numpy
#   安装：pip install biopython pandas numpy

import subprocess
import os
import pandas as pd

# 有参考基因组 RNA-seq 两种策略 + ChIP-seq 分析（Python 封装演示）

def strategy_align_then_assemble(r1, r2, genome_index, ref_gtf):
    """策略A: 先匹配再组装"""
    print("=== 策略A: align-then-assemble ===")
    cmd1 = f"hisat2 -x {genome_index} -1 {r1} -2 {r2} -S aln.sam"
    cmd2 = f"samtools sort -o aln.bam aln.sam"
    cmd3 = f"stringtie aln.bam -G {ref_gtf} -o merged.gtf"
    print(f"[A1] {cmd1}")
    print(f"[A2] {cmd2}")
    print(f"[A3] {cmd3}")
    # subprocess.run(cmd1, shell=True, check=True)
    # subprocess.run(cmd2, shell=True, check=True)
    # subprocess.run(cmd3, shell=True, check=True)
    return "merged.gtf"

def strategy_assemble_then_align(r1, r2, genome_index):
    """策略B: 先组装再匹配"""
    print("=== 策略B: assemble-then-align ===")
    cmd1 = f"trinity --seqType fq --left {r1} --right {r2} --output trinity_out"
    cmd2 = f"gmap -d {genome_index} trinity_out/Trinity.fasta > asm.sam"
    print(f"[B1] {cmd1}")
    print(f"[B2] {cmd2}")
    # subprocess.run(cmd1, shell=True, check=True)
    # subprocess.run(cmd2, shell=True, check=True)
    return "asm.sam"

def chipseq_analysis(chip_fq, input_bam, genome_index, repeats_bed):
    """ChIP-seq 分析"""
    print("=== ChIP-seq 分析 ===")
    cmd1 = f"bowtie2 -x {genome_index} -U {chip_fq} -S chip.sam"
    cmd2 = f"samtools sort -o chip.bam chip.sam"
    cmd3 = f"macs2 callpeak -t chip.bam -c {input_bam} -g hs -n peak"
    cmd4 = f"bedtools intersect -a chip.bam -b {repeats_bed} -c"
    print(f"[C1] {cmd1}")
    print(f"[C2] {cmd2}")
    print(f"[C3] {cmd3}")
    print(f"[C4] {cmd4}")
    # subprocess.run(cmd1, shell=True, check=True)
    # subprocess.run(cmd2, shell=True, check=True)
    # subprocess.run(cmd3, shell=True, check=True)
    # subprocess.run(cmd4, shell=True, check=True)
    return "peak_peaks.narrowPeak"

if __name__ == "__main__":
    r1, r2 = "r1.fq", "r2.fq"
    genome_index = "genome_index"
    ref_gtf = "ref.gtf"
    strategy_align_then_assemble(r1, r2, genome_index, ref_gtf)
    strategy_assemble_then_align(r1, r2, genome_index)
    chipseq_analysis("chip.fq", "input.bam", genome_index, "repeats.bed")
    print("\n所有分析演示完成。时间复杂度：比对 O(N*M)，Peak calling O(N log N)")

