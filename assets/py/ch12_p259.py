# -*- coding: utf-8 -*-
# 损失函数、经验风险最小化与Fisher经典参数统计理论（ch12 p259）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：numpy。安装命令：pip install numpy 或 conda install numpy

import numpy as np

# 设置随机种子，保证结果可复现
np.random.seed(42)

def empirical_risk_squared(y, X, w):
    """平方损失下的经验风险：mean((y - Xw)^2)"""
    pred = X @ w                      # 模型预测值 f(x, w) = Xw
    return np.mean((y - pred) ** 2)   # 对每个样本的平方误差取平均

def empirical_risk_misclassification(y_true, y_pred):
    """分类问题：经验风险 = 训练错误率"""
    return np.mean(y_true != y_pred)  # 预测错误的样本比例

def negative_log_likelihood(log_probs):
    """密度估计：负对数似然"""
    return -np.mean(log_probs)        # 平均负对数似然

# 极简示例
n, m = 50, 3
X = np.random.randn(n, m)             # 50 个样本，3 个特征
y = np.random.randn(n)                # 连续型因变量
w = np.zeros(m)                       # 初始权重全为 0

risk = empirical_risk_squared(y, X, w)
print('平方损失经验风险（w=0）:', risk)

# 分类示例
y_true = np.array([0, 1, 1, 0, 1])
y_pred = np.array([0, 1, 0, 0, 1])
print('分类错误率:', empirical_risk_misclassification(y_true, y_pred))

# 密度估计示例
log_probs = np.log(np.array([0.8, 0.6, 0.9, 0.7]))
print('负对数似然:', negative_log_likelihood(log_probs))

