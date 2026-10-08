# -*- coding: utf-8 -*-
# PAM打分矩阵与PAM值选择（ch03 p46）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8（无第三方依赖）
#   可选：pip install biopython numpy

def choose_pam(identity_percent):
    # identity_percent: 两条序列的相似度百分比
    if identity_percent >= 85:
        return 'PAM1~PAM50'
    elif identity_percent >= 60:
        return 'PAM100~PAM150'
    elif identity_percent >= 40:
        return 'PAM200'
    else:
        return 'PAM250'

if __name__ == '__main__':
    print(choose_pam(70))  # 预期 'PAM100~PAM150'
    print(choose_pam(30))  # 预期 'PAM250'
    print(choose_pam(90))  # 预期 'PAM1~PAM50'
    print(choose_pam(50))  # 预期 'PAM200'

