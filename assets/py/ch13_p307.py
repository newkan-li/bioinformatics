# -*- coding: utf-8 -*-
# BioPerl 序列特征与标签系统（ch13 p307）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：biopython。安装：pip install biopython 或 conda install -c conda-forge biopython。

from Bio import SeqIO

# 创建示例 GenBank 文件（含特征）
import os
if not os.path.exists('input_feat.gb'):
    with open('input_feat.gb', 'w') as f:
        f.write('LOCUS       TEST0002        30 bp    DNA     linear   UNC 01-JAN-2000\n')
        f.write('DEFINITION  Test with features.\n')
        f.write('ACCESSION   TEST0002\n')
        f.write('VERSION     TEST0002.1\n')
        f.write('FEATURES             Location/Qualifiers\n')
        f.write('     source          1..30\n')
        f.write('                     /organism=\"synthetic\"\n')
        f.write('     gene            1..30\n')
        f.write('                     /gene=\"geneX\"\n')
        f.write('     CDS             1..30\n')
        f.write('                     /product=\"hypothetical protein\"\n')
        f.write('ORIGIN\n')
        f.write('        1 atgcatgcat gcatgcatgc atgcatgcat\n')
        f.write('//\n')

# 读取序列
record = SeqIO.read('input_feat.gb', 'genbank')

# 1. 特征数量
feature_count = len(record.features)
print(f'Feature count: {feature_count}')

# 2. 遍历所有特征
for feat in record.features:
    # 3. 输出起止位置
    print(feat.type, '\t', feat.location)

    # 4. 获取所有标签
    for tag in feat.qualifiers:
        # 5. 获取标签值
        values = feat.qualifiers[tag]
        print(f'  {tag} = {", ".join(values)}')

    # 6. 主标签（type）
    print(f'  primary_tag: {feat.type}')

# 示例输出类似：
# join(TEST0002.1:1..30)

