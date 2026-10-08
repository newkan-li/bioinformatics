# -*- coding: utf-8 -*-
# Perl 哈希表操作、正则表达式与替换（ch13 p299）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（仅使用标准库）。如需安装可选包：pip install numpy

# 数组排序与删除
arr = [3, 1, 4, 1, 5]
sorted_arr = sorted(arr)  # 升序排序，返回新列表
print('sorted:', sorted_arr)

# 删除下标2的元素
del arr[2]
print('after del index 2:', arr)

# 清空数组
arr.clear()  # 清空列表
print('after clear:', arr)

# 哈希表操作（Python 用 dict）
h = {'a': 1, 'b': 2, 'c': 3}
h['d'] = 4  # 添加
print('h:', h)

# 合并字典
h2 = {**h, 'e': 5}
print('h2:', h2)

# 循环哈希
for k, v in h.items():
    print(f'{k}={v}')

for k in h.keys():
    print(f'{k} => {h[k]}')

# 排序哈希
for k in sorted(h.keys()):
    print(f'{k} => {h[k]}')

# 删除元素
del h['b']
print('after delete b:', h)
