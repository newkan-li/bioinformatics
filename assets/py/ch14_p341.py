# -*- coding: utf-8 -*-
# RNA-seq生物信息学分析流程（无参考基因组与有参考基因组）（ch14 p341）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, pandas, numpy
#   安装：pip install biopython pandas numpy

import subprocess
import os
import pandas as pd
import numpy as np

# RNA-seq 无参考基因组分析流程（Python 封装演示）
# 输入: reads.fq
# 输出: unigene 表达矩阵 + 注释

def step_fastqc(reads_fq):
    """1. 质量评估"""
    cmd = f"fastqc {reads_fq}"
    print(f"[Step1] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return f"{reads_fq}_fastqc.html"

def step_trim(reads_fq):
    """2. 去冗余、去接头"""
    cmd = f"trimmomatic SE {reads_fq} trimmed.fq"
    print(f"[Step2] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "trimmed.fq"

def step_trinity(reads_fq, cpu=8):
    """3. de novo 组装"""
    cmd = f"trinity --seqType fq --left {reads_fq} --CPU {cpu} --output trinity_out"
    print(f"[Step3] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "trinity_out/Trinity.fasta"

def step_cdhit(trinity_fasta, identity=0.95):
    """4. 去冗余得到 Unigene"""
    cmd = f"cd-hit-est -i {trinity_fasta} -o unigene.fasta -c {identity}"
    print(f"[Step4] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "unigene.fasta"

def step_blastx(unigene_fasta):
    """5. 功能注释"""
    cmd = f"blastx {unigene_fasta} -db nr -out blast.out"
    print(f"[Step5] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "blast.out"

def step_go_annotation(unigene_fasta):
    """6. GO 分类"""
    cmd = f"blast2go {unigene_fasta}"
    print(f"[Step6] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "go_annotation.txt"

def step_kegg(unigene_fasta):
    """7. 代谢通路"""
    cmd = f"kegg_annotation {unigene_fasta}"
    print(f"[Step7] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "kegg_annotation.txt"

def step_quantify(reads_fq, unigene_fasta):
    """8. 表达定量"""
    cmd = f"salmon quant -i {unigene_fasta} -r {reads_fq} -o quant_out"
    print(f"[Step8] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "quant_out/quant.sf"

def step_diff_expr(quant_file):
    """9. 差异表达"""
    cmd = f"edgeR {quant_file}"
    print(f"[Step9] {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return "diff_expr.csv"

if __name__ == "__main__":
    reads = "reads.fq"
    print("=== RNA-seq 无参考基因组分析流程 ===")
    step_fastqc(reads)
    trimmed = step_trim(reads)
    trinity_fa = step_trinity(trimmed)
    unigene = step_cdhit(trinity_fa)
    step_blastx(unigene)
    step_go_annotation(unigene)
    step_kegg(unigene)
    step_quantify(trimmed, unigene)
    step_diff_expr("quant_out/quant.sf")
    print("\n流程演示完成。时间复杂度：组装 O(N log N) ~ O(N^2)，比对 O(N*M)")

