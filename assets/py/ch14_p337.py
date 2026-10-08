# -*- coding: utf-8 -*-
# 小RNA测序、lncRNA测序及ChIP-seq（ch14 p337）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：biopython, pandas, numpy, scipy, matplotlib, pysam, cutadapt (可选), fastqc (可选), bowtie (可选), miRDeep2 (可选), DESeq2 (R包，需rpy2或独立R环境)。安装命令：
#   pip install biopython pandas numpy scipy matplotlib pysam rpy2
#   conda install -c bioconda fastqc cutadapt bowtie mirdeep2
#   # 对于DESeq2，建议在R中安装：install.packages('DESeq2') 或 BiocManager::install('DESeq2')

import subprocess
import os
import pandas as pd
import numpy as np
from Bio import SeqIO
import pysam

# 1. 质控 (调用FastQC)
def run_fastqc(input_fastq, outdir='fastqc_out'):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['fastqc', input_fastq, '-o', outdir], check=True)
    print(f'FastQC report saved to {outdir}')

# 2. 去除接头 (调用cutadapt)
def trim_adapters(input_fastq, output_fastq, adapter='TGGAATTCTCGGGTGCCAAGG'):
    subprocess.run(['cutadapt', '-a', adapter, '-o', output_fastq, input_fastq], check=True)
    print(f'Trimmed reads saved to {output_fastq}')

# 3. 比对到参考基因组 (调用bowtie)
def align_bowtie(genome_index, trimmed_fastq, output_bam):
    # bowtie 输出 SAM，需转换为 BAM 并排序
    sam_file = output_bam.replace('.bam', '.sam')
    subprocess.run(['bowtie', '-f', '-v', '1', '-m', '1', '--best', '--strata',
                    genome_index, trimmed_fastq, sam_file], check=True)
    # 转换 SAM 到 BAM
    pysam.view('-bS', '-o', output_bam, sam_file, catch_stdout=False)
    pysam.sort('-o', output_bam, output_bam)  # 排序
    os.remove(sam_file)
    print(f'Aligned BAM saved to {output_bam}')

# 4. 鉴定已知microRNA (调用miRDeep2)
def identify_mirna(trimmed_fastq, genome_fa, aligned_bam, mature_miRNA_fa, output_dir='mirdeep_out'):
    os.makedirs(output_dir, exist_ok=True)
    # miRDeep2 需要 reads 为 fasta 格式，先转换
    reads_fa = os.path.join(output_dir, 'reads.fa')
    with open(trimmed_fastq) as f_in, open(reads_fa, 'w') as f_out:
        for record in SeqIO.parse(f_in, 'fastq'):
            f_out.write(f'>{record.id}\n{record.seq}\n')
    # 运行 miRDeep2
    subprocess.run(['miRDeep2.pl', reads_fa, genome_fa, aligned_bam,
                    mature_miRNA_fa, 'none', 'none', 'none'],
                   cwd=output_dir, check=True)
    print(f'miRDeep2 results in {output_dir}')

# 5. 差异表达分析 (使用pandas模拟DESeq2的输入，实际分析需R)
def prepare_deseq2_input(count_matrix_file, coldata_file):
    # 读取计数矩阵和样本信息
    counts = pd.read_csv(count_matrix_file, index_col=0)
    coldata = pd.read_csv(coldata_file, index_col=0)
    print('Count matrix shape:', counts.shape)
    print('Coldata shape:', coldata.shape)
    # 保存为DESeq2可读格式
    counts.to_csv('deseq2_counts.csv')
    coldata.to_csv('deseq2_coldata.csv')
    print('Files ready for DESeq2 in R.')

if __name__ == '__main__':
    # 示例运行（需提前准备文件）
    # run_fastqc('smallRNA.fastq')
    # trim_adapters('smallRNA.fastq', 'trimmed.fastq')
    # align_bowtie('genome_index', 'trimmed.fastq', 'aligned.bam')
    # identify_mirna('trimmed.fastq', 'genome.fa', 'aligned.bam', 'mature_miRNA.fa')
    # prepare_deseq2_input('counts.csv', 'coldata.csv')
    print('Pipeline functions defined. Uncomment to run with your data.')
