# -*- coding: utf-8 -*-
# NGS数据分析的主要生物信息学工具（ch14 p340）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, pandas
#   安装：pip install biopython pandas

import subprocess
import os
import pandas as pd

# 模拟 NGS 常用工具命令的 Python 封装
# 注意：以下命令需要相应工具已安装，这里仅演示如何用 Python 调用

def run_velvet(reads_fastq, output_dir, kmer=21):
    """Velvet 短片段组装"""
    # velveth: 构建哈希表
    cmd1 = f"velveth {output_dir} {kmer} -fastq {reads_fastq}"
    # velvetg: 构建组装图
    cmd2 = f"velvetg {output_dir} -cov_cutoff auto"
    print(f"[Velvet] 执行: {cmd1}")
    print(f"[Velvet] 执行: {cmd2}")
    # 实际运行时取消注释：
    # subprocess.run(cmd1, shell=True, check=True)
    # subprocess.run(cmd2, shell=True, check=True)
    return os.path.join(output_dir, "contigs.fa")

def run_euler(reads_fasta, output_prefix):
    """EULER 混合片段组装"""
    cmd = f"euler -reads {reads_fasta} -output {output_prefix}"
    print(f"[EULER] 执行: {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return f"{output_prefix}.fasta"

def run_mosaik(reference_fa, reads_fastq, out_bam):
    """MOSAIK NGS 序列匹配"""
    cmd = f"mosaik align -ref {reference_fa} -in {reads_fastq} -out {out_bam}"
    print(f"[MOSAIK] 执行: {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return out_bam

def run_rmap(reference_fa, reads_fastq, output_txt):
    """RMAP 短片段匹配到参考基因组"""
    cmd = f"rmap -h {reference_fa} {reads_fastq} > {output_txt}"
    print(f"[RMAP] 执行: {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return output_txt

def run_sharcgs(reads_fasta, output_prefix):
    """SHARCGS 短片段重组装"""
    cmd = f"sharcgs -reads {reads_fasta} -o {output_prefix}"
    print(f"[SHARCGS] 执行: {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return f"{output_prefix}.fasta"

def run_soap(reads_fastq, reference_fa, output_soap, threads=4):
    """SOAP 片段匹配"""
    cmd = f"soap -a {reads_fastq} -d {reference_fa} -o {output_soap} -p {threads}"
    print(f"[SOAP] 执行: {cmd}")
    # subprocess.run(cmd, shell=True, check=True)
    return output_soap

if __name__ == "__main__":
    # 演示调用（不会真正执行外部命令，只打印）
    run_velvet("reads.fastq", "velvet_out", kmer=21)
    run_euler("reads.fasta", "euler_assembly")
    run_mosaik("reference.fa", "reads.fastq", "aligned.bam")
    run_rmap("reference.fa", "reads.fastq", "output.txt")
    run_sharcgs("reads.fasta", "sharcgs_assembly")
    run_soap("reads.fastq", "reference.fa", "output.soap", threads=4)
    print("\n所有工具命令演示完成。")

