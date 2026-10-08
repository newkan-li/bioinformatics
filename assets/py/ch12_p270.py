# -*- coding: utf-8 -*-
# 判别函数的F检验与贝叶斯推理引论（ch12 p270）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   pip install numpy scipy

import numpy as np
from scipy.stats import f

def discriminant_f_test(nA, nB, p, between_var, within_var, alpha=0.05):
    """
    nA, nB: 两类样本数
    p: 变量数
    between_var: 组间差异
    within_var: 组内差异
    """
    F = between_var / within_var          # 计算 F 统计量
    df1 = p                               # 分子自由度
    df2 = nA + nB - p - 1                 # 分母自由度
    F_crit = f.ppf(1 - alpha, df1, df2)   # 临界值
    return F, F_crit, F > F_crit          # 返回 F 值、临界值、是否显著

# 极简示例
F, F_crit, significant = discriminant_f_test(
    nA=20, nB=20, p=3, between_var=12.5, within_var=2.5
)
print(F, F_crit, significant)

# 时间复杂度：O(1)
