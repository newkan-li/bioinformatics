# -*- coding: utf-8 -*-
# BLOSUM打分矩阵的构建与特点（ch03 p47）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8（无第三方依赖）
#   可选：pip install biopython

def choose_blosum(identity_percent):
    # 根据序列相似度选择 BLOSUM 编号
    if identity_percent >= 80:
        return 'BLOSUM80'
    elif identity_percent >= 62:
        return 'BLOSUM62'
    elif identity_percent >= 45:
        return 'BLOSUM45'
    else:
        return 'BLOSUM30'

if __name__ == '__main__':
    print(choose_blosum(75))  # 预期 'BLOSUM62'
    print(choose_blosum(90))  # 预期 'BLOSUM80'
    print(choose_blosum(50))  # 预期 'BLOSUM45'
    print(choose_blosum(30))  # 预期 'BLOSUM30'

