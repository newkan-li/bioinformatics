# -*- coding: utf-8 -*-
# 4D核体计划与Hi-C技术流程（ch14 p347）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：numpy, scipy。安装：pip install numpy scipy

import numpy as np
from scipy.linalg import inv

# Hi-C 数据处理核心步骤（Python 实现）
# 输入: paired-end reads (R1.fq, R2.fq), reference genome
# 输出: contact matrix

def bowtie2(r1, r2, genome):
    """模拟比对，返回比对结果"""
    # 实际使用 bowtie2 命令
    return np.random.randint(0, 1000, size=(100, 2))  # 模拟100对reads的比对位置

def filter_pairs(alignments):
    """过滤未比对、多比对、PCR重复"""
    # 简单模拟：保留前80%
    return alignments[:int(len(alignments)*0.8)]

def re_align_to_restriction_sites(pairs):
    """酶切位点附近重新定位"""
    # 模拟：位置微调
    return pairs + np.random.randint(-5, 5, size=pairs.shape)

def assign_bins(pairs, bin_size=1_000_000):
    """按基因组 bin 划分"""
    bins = pairs // bin_size
    return bins

def build_contact_matrix(bins):
    """构建接触矩阵"""
    max_bin = bins.max() + 1
    matrix = np.zeros((max_bin, max_bin), dtype=int)
    for i in range(len(bins)):
        b1, b2 = bins[i]
        matrix[b1, b2] += 1
        matrix[b2, b1] += 1  # 对称
    return matrix

def ice_normalize(matrix, max_iter=100, tol=1e-5):
    """ICE 归一化"""
    m = matrix.astype(float)
    # 避免除零
    m[m == 0] = 1e-10
    for _ in range(max_iter):
        row_sums = m.sum(axis=1)
        # 计算偏差
        bias = row_sums / row_sums.mean()
        # 更新矩阵
        m_new = m / np.outer(bias, bias)
        # 检查收敛
        if np.allclose(m, m_new, atol=tol):
            break
        m = m_new
    return m

def hic_pipeline(r1, r2, genome):
    """完整 Hi-C 流程"""
    # 1. 比对
    alignments = bowtie2(r1, r2, genome)
    print(f"比对结果形状: {alignments.shape}")
    
    # 2. 过滤
    valid_pairs = filter_pairs(alignments)
    print(f"过滤后形状: {valid_pairs.shape}")
    
    # 3. 酶切位点重新定位
    pairs = re_align_to_restriction_sites(valid_pairs)
    
    # 4. 分箱
    bins = assign_bins(pairs, bin_size=1_000_000)
    print(f"分箱后形状: {bins.shape}, 最大bin: {bins.max()}")
    
    # 5. 构建接触矩阵
    matrix = build_contact_matrix(bins)
    print(f"接触矩阵形状: {matrix.shape}")
    
    # 6. 归一化
    matrix_norm = ice_normalize(matrix)
    
    return matrix_norm

# 极简示例：3 个 bin 的接触矩阵
matrix = np.array([[10, 3, 1],
                   [3, 8, 2],
                   [1, 2, 5]])
print("原始矩阵:")
print(matrix)

# 归一化
norm_matrix = ice_normalize(matrix)
print("\nICE 归一化后:")
print(norm_matrix)

# 运行完整流程
print("\n运行完整 Hi-C 流程:")
result = hic_pipeline("R1.fq", "R2.fq", "genome.fa")
print(f"\n最终矩阵形状: {result.shape}")

# 时间复杂度总览
print("\n时间复杂度总览:")
print("比对 O(N*L), 过滤 O(N), 分箱 O(N), 矩阵 O(N+B^2), 归一化 O(B^3)")

