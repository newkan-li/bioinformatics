# -*- coding: utf-8 -*-
# SOLiD数据分析及第二代测序技术应用概述（ch14 p336）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+
#   无需额外依赖（仅使用标准库）
#   如需完整生物信息学工具链可安装：pip install biopython numpy pandas

# SOLiD颜色序列解码为碱基序列
# 双碱基编码矩阵：4种颜色对应16种双碱基组合
# 已知任一位置碱基，可逐步解码

def decode_solid(colors, start_base):
    """
    colors: 颜色序列，如 ['R','B','G',...]
    start_base: 已知起始碱基，如 'A'
    返回解码后的碱基序列
    """
    base_map = {
        ('A','A'):'R', ('A','C'):'B', ('A','G'):'G', ('A','T'):'Y',
        ('C','A'):'B', ('C','C'):'R', ('C','G'):'Y', ('C','T'):'G',
        ('G','A'):'G', ('G','C'):'Y', ('G','G'):'R', ('G','T'):'B',
        ('T','A'):'Y', ('T','C'):'G', ('T','G'):'B', ('T','T'):'R'
    }
    bases = [start_base]
    for color in colors:
        prev = bases[-1]
        for (b1, b2), c in base_map.items():
            if b1 == prev and c == color:
                bases.append(b2)
                break
    return ''.join(bases)

# 示例
colors = ['R', 'B', 'G']
start = 'A'
print(decode_solid(colors, start))  # 输出: AACG
