# -*- coding: utf-8 -*-
# 多因素数据统计分析、RASH及NGS数据获取（ch14 p339）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：pandas, numpy, scipy, matplotlib, statsmodels。安装命令：
#   pip install pandas numpy scipy matplotlib statsmodels

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# 1. 双因素方差分析 (模拟R的aov)
def two_way_anova():
    # 创建数据框
    df = pd.DataFrame({
        'expr': [10,12,15,9,11,14,20,22,25,19,21,24],
        'factorA': ['ctrl']*6 + ['treat']*6,
        'factorB': ['cond1','cond2','cond3']*4
    })
    # 确保因子为分类变量
    df['factorA'] = df['factorA'].astype('category')
    df['factorB'] = df['factorB'].astype('category')
    # 拟合模型
    model = ols('expr ~ C(factorA) * C(factorB)', data=df).fit()
    # 方差分析表
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)
    return df

# 2. RASH：相关性聚类
def rash_clustering():
    # 模拟基因表达矩阵（行=基因，列=样品）
    np.random.seed(42)
    expr_matrix = pd.DataFrame(np.random.rand(10, 5),
                               columns=['S1','S2','S3','S4','S5'],
                               index=[f'G{i}' for i in range(1,11)])
    # 计算样品间相关性
    corr = expr_matrix.corr()
    print('Correlation matrix:')
    print(corr)
    # 层次聚类
    Z = linkage(corr, method='average')
    # 绘制树状图
    plt.figure(figsize=(8, 6))
    dendrogram(Z, labels=corr.columns)
    plt.title('Sample Clustering Dendrogram')
    plt.xlabel('Samples')
    plt.ylabel('Distance')
    plt.show()
    return corr

if __name__ == '__main__':
    print('Two-way ANOVA:')
    two_way_anova()
    print('\nRASH clustering:')
    rash_clustering()
