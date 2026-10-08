# -*- coding: utf-8 -*-
# Perl 内置函数：数学、哈希与列表处理（ch13 p301）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（仅使用标准库）。

import math

# 数学函数
deg = 60
rad = math.radians(deg)  # 角度转弧度
print(math.cos(rad))
print(math.sin(rad))
print(math.atan2(1, 1))

# 哈希函数（字典操作）
h = {'a': 1, 'b': 2, 'c': 3}
for k, v in h.items():
    print(f'{k}={v}')

keys = list(h.keys())
vals = list(h.values())
print(keys)
print(vals)

# grep 与 map
nums = list(range(1, 11))
even = [x for x in nums if x % 2 == 0]  # 过滤偶数
squares = [x * x for x in nums]  # 平方
print('even:', even)
print('squares:', squares)

# join
str_ = ','.join(map(str, even))
print(str_)
