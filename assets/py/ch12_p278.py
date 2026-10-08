# -*- coding: utf-8 -*-
# HMM基因识别程序及HMM优缺点（ch12 p278）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（纯标准库）。如需生物信息学工具可安装：pip install biopython

# 模拟 HMM 基因识别程序的命令行调用与优缺点总结
# 注意：以下命令为示例，实际运行需安装对应软件

import subprocess

def run_cmd(cmd):
    print('Running:', cmd)
    # subprocess.run(cmd, shell=True)  # 实际执行时取消注释

# VEIL
run_cmd('veil -i human_seq.fa -o veil.gff')

# HMMgene
run_cmd('hmmgene -m human -p 0.99 -i seq.fa > hmmgene.gff')

# GeneMark.hmm
run_cmd('gmhmme -m Arabidopsis -f gff -o out.gff seq.fa')

# Geneie
run_cmd('geneie -seq seq.fa -org human -out geneie.gff')

# GENSCAN
run_cmd('genscan seq.fa > genscan.out')

# 优缺点总结
pros  = ['probabilistic framework', 'handles variable-length features',
         'trainable from data']
cons  = ['independence assumption', 'sensitive to training set',
         'hard to model long-range dependencies']

print('Pros:')
for p in pros:
    print(' -', p)
print('Cons:')
for c in cons:
    print(' -', c)
