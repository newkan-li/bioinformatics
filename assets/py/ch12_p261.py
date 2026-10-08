# -*- coding: utf-8 -*-
# 结构风险最小化（SRM）原则（ch12 p261）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np

# 计算 VC 置信界（示意形式）
def confidence_term(h, n, delta=0.05):
    # h: VC 维（模型复杂度），n: 样本数，delta: 置信参数
    return np.sqrt((h * (np.log(2 * n / h) + 1) - np.log(delta / 4)) / n)

# 结构风险 = 经验风险 + 置信范围
def structural_risk(empirical_risk, h, n, delta=0.05):
    return empirical_risk + confidence_term(h, n, delta)

# 极简示例：固定经验风险，观察不同复杂度 h 下的结构风险
n = 1000
for h in [5, 20, 100]:
    print(h, structural_risk(0.1, h, n))
