# -*- coding: utf-8 -*-
# 朴素贝叶斯分类计算与隐马尔可夫模型引入（ch12 p272）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8
#   无需额外安装（仅使用标准库）

# 气候训练集朴素贝叶斯计算示例
P_N = 5/14
P_P = 9/14

P_Sunny_N = 3/5
P_Hot_N = 2/5
P_High_N = 4/5
P_Weak_N = 2/5

P_Sunny_P = 2/9
P_Hot_P = 2/9
P_High_P = 3/9
P_Weak_P = 6/9

score_N = P_N * P_Sunny_N * P_Hot_N * P_High_N * P_Weak_N
score_P = P_P * P_Sunny_P * P_Hot_P * P_High_P * P_Weak_P

print(score_N)  # 0.0274
print(score_P)  # 0.007039

pred = 'N' if score_N > score_P else 'P'
print(pred)

# 时间复杂度：O(m * d)
