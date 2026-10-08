# -*- coding: utf-8 -*-
# 新技术相互关系与生物信息学挑战（ch14 p348）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：numpy, scikit-learn, pandas, matplotlib。安装：pip install numpy scikit-learn pandas matplotlib

import numpy as np
from sklearn.cluster import SpectralClustering
import pandas as pd
import matplotlib.pyplot as plt

# 示例：用 Hi-C 接触信号对宏基因组 contigs 聚类
def cluster_contigs_by_hic(contact_matrix, n_clusters):
    """
    contact_matrix: contig 间 Hi-C 接触矩阵 (C x C)
    n_clusters: 预期物种数
    返回: 每个 contig 的物种标签
    """
    # 归一化
    norm = contact_matrix / contact_matrix.sum(axis=1, keepdims=True)
    # 谱聚类
    sc = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', random_state=42)
    labels = sc.fit_predict(norm)
    return labels

# 模拟数据：5 个 contig，2 个物种
np.random.seed(42)
contact_matrix = np.array([
    [10, 8, 1, 0, 0],
    [8, 12, 2, 1, 0],
    [1, 2, 9, 7, 1],
    [0, 1, 7, 11, 2],
    [0, 0, 1, 2, 6]
])

print("接触矩阵:")
print(contact_matrix)

# 聚类
n_clusters = 2
labels = cluster_contigs_by_hic(contact_matrix, n_clusters)
print(f"\n聚类标签: {labels}")

# 可视化
plt.figure(figsize=(8, 6))
plt.imshow(contact_matrix, cmap='hot', interpolation='nearest')
plt.colorbar(label='接触频率')
plt.title('Hi-C 接触矩阵热图')
plt.xlabel('Contig 索引')
plt.ylabel('Contig 索引')
plt.savefig('hic_contact_matrix.png')
print("热图已保存为 hic_contact_matrix.png")

# 数据存储挑战示例
print("\n数据存储挑战:")
print("- 原始图像数据：可舍弃，节省 PB 级存储")
print("- 序列数据：需长期保存，建议压缩（CRAM / zstd）")
print("Linux 示例:")
print("samtools view -C -T ref.fa input.bam > output.cram")
print("zstd -19 reads.fastq -o reads.fastq.zst")

# 时间复杂度
print("\n时间复杂度：谱聚类 O(C^3)，C=contig 数")

