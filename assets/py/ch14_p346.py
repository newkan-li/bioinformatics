# -*- coding: utf-8 -*-
# 人类微生物组计划、细胞微环境与三维基因组学（ch14 p346）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：biopython, pandas, numpy, matplotlib。安装：pip install biopython pandas numpy matplotlib

import subprocess
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 模拟 HMP 宏基因组分析流程（用 Python 调用外部工具并解析结果）
# 注意：实际运行需要安装 wget, fastqc, trimmomatic, bowtie2, kraken2, humann2, hicup
# 这里用模拟数据演示流程和结果解析

def run_cmd(cmd):
    """运行 shell 命令并返回输出"""
    print(f"运行: {cmd}")
    # 实际运行时取消注释下一行
    # result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    # return result.stdout
    return "模拟输出"

# 1. 下载数据（模拟）
print("步骤1: 下载 HMP 数据")
# run_cmd("wget http://www.hmpdacc.org/data/sample.fq")

# 2. 质量控制
print("步骤2: 质量控制")
# run_cmd("fastqc sample.fq")
# run_cmd("trimmomatic PE sample_1.fq sample_2.fq out_1.fq out_2.fq")

# 3. 去宿主
print("步骤3: 去宿主")
# run_cmd("bowtie2 -x human_genome -1 out_1.fq -2 out_2.fq --un nonhuman.fq")

# 4. 物种注释
print("步骤4: 物种注释")
# run_cmd("kraken2 --db minikraken nonhuman.fq --output kraken.out")

# 5. 功能注释
print("步骤5: 功能注释")
# run_cmd("humann2 --input nonhuman.fq --output humann2_out")

# 6. 三维基因组学 (Hi-C)
print("步骤6: Hi-C 分析")
# run_cmd("hicup --index genome_index --digest genome_digest reads.fq")

# 模拟 Kraken2 输出解析
kraken_data = {
    'taxon': ['Bacteria', 'Archaea', 'Viruses', 'Eukaryota', 'Unclassified'],
    'count': [15000, 2000, 500, 300, 1200]
}
df = pd.DataFrame(kraken_data)
df['percentage'] = df['count'] / df['count'].sum() * 100
print("\n物种注释结果:")
print(df)

# 绘制物种组成饼图
plt.figure(figsize=(8, 6))
plt.pie(df['count'], labels=df['taxon'], autopct='%1.1f%%')
plt.title('HMP 宏基因组物种组成')
plt.savefig('hmp_species.png')
print("\n饼图已保存为 hmp_species.png")

# 时间复杂度说明
print("\n时间复杂度:")
print("比对: O(N*M), N=reads数, M=参考基因组大小")
print("Kraken: O(N), N=reads数")

