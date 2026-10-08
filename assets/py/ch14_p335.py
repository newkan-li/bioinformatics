# -*- coding: utf-8 -*-
# SOLiD连接测序原理（ch14 p335）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+
#   无需额外依赖（仅使用标准库）
#   如需扩展可安装：pip install biopython

# SOLiD 连接测序原理模拟（极简）
# 模拟连接测序循环：探针连接、记录颜色、断裂、进入下一轮

# 模拟模板序列
template = "ACGTACGT"

# 模拟探针编码区第1、2位与颜色的对应关系
probe_color_map = {
    "AC": "红", "CA": "红", "GT": "红", "TG": "红",
    "AG": "蓝", "GA": "蓝", "CT": "蓝", "TC": "蓝",
    "AT": "绿", "TA": "绿", "CG": "绿", "GC": "绿",
    "AA": "黄", "CC": "黄", "GG": "黄", "TT": "黄"
}

# 模拟测序循环
colors = []
read_length = len(template) - 1  # 每次读取一个双碱基编码

for i in range(read_length):
    dinuc = template[i:i+2]          # 当前探针编码区第1、2位
    color = probe_color_map[dinuc]   # 记录颜色
    colors.append(color)
    print(f"第{i+1}轮: 探针编码区={dinuc}, 颜色={color}")

print("颜色序列:", colors)

# 时间复杂度：O(L)，L为读长
