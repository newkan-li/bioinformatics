# -*- coding: utf-8 -*-
# 朴素贝叶斯分类器与气候训练集示例（ch12 p271）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   pip install numpy pandas

import numpy as np
import pandas as pd

# 构造气候训练集
data = pd.DataFrame({
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
                    'Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal',
                 'High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'Play': ['N','N','P','P','P','P','P','N','P','P','P','P','P','N']
})

# 测试样本
X = {'Outlook':'Sunny','Temperature':'Hot','Humidity':'High','Wind':'Weak'}

# 计算先验概率
priors = data['Play'].value_counts(normalize=True).to_dict()
print('Priors:', priors)

# 计算条件概率
likelihoods = {}
for c in priors:
    subset = data[data['Play'] == c]
    likelihoods[c] = {}
    for attr, val in X.items():
        # 拉普拉斯平滑，避免零概率
        count = ((subset[attr] == val).sum() + 1) / (len(subset) + data[attr].nunique())
        likelihoods[c][attr] = count

# 计算后验得分
scores = {}
for c in priors:
    score = priors[c]
    for attr in X:
        score *= likelihoods[c][attr]
    scores[c] = score

print('Scores:', scores)
pred = max(scores, key=scores.get)
print('Prediction:', pred)
