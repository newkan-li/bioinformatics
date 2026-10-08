# -*- coding: utf-8 -*-
# 系统聚类步骤与类间距离（ch12 p267）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np

def single_linkage(D, labels):
    # 复制距离矩阵并转为浮点，避免修改原数据
    D = D.astype(float).copy()
    # 对角线设为无穷大，防止自己与自己合并
    np.fill_diagonal(D, np.inf)
    # 初始化每个样本为一个簇，键为簇编号，值为成员列表
    clusters = {i: [i] for i in range(len(labels))}
    active = set(clusters)
    # 循环直到只剩一个簇
    while len(active) > 1:
        best = None
        # 遍历所有活跃簇对，找最小类间距离
        for i in active:
            for j in active:
                if i < j and (best is None or D[i, j] < best[0]):
                    best = (D[i, j], i, j)
        _, i, j = best
        # 合并簇 j 到簇 i
        clusters[i] += clusters[j]
        active.remove(j)
        # 最短距离法更新：新簇 i 与其他簇 k 的距离取 min(D[i,k], D[j,k])
        for k in active:
            if k != i:
                D[i, k] = D[k, i] = min(D[i, k], D[j, k])
    return clusters

# 示例距离矩阵
D = np.array([[0, 1, 4],
              [1, 0, 2],
              [4, 2, 0]])
print(single_linkage(D, ['A', 'B', 'C']))

# 时间复杂度：朴素实现 O(n^3)，优化后可 O(n^2 log n)
