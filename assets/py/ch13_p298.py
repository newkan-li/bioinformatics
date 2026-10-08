# -*- coding: utf-8 -*-
# Perl 字符串比较、数组操作与哈希表初步（ch13 p298）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外第三方包（仅使用标准库）。

# Perl 字符串比较的 Python 等价实现
# 注意：Python 中字符串比较使用 ==、!=、<、> 等运算符，
# 而 Perl 使用 eq、ne、cmp、lt 等。

a = "abc"
b = "abd"

print(a == b)   # False，对应 Perl 的 $a eq $b
print(a != b)   # True，对应 Perl 的 $a ne $b
print((a > b) - (a < b))  # -1，对应 Perl 的 $a cmp $b
print(a < b)    # True，对应 Perl 的 $a lt $b

# 数组创建
arr1 = [1, 2, 3]
arr2 = list(range(1, 6))  # [1, 2, 3, 4, 5]
arr3 = ["apple", "banana", "cherry"]

# 合并数组
merged = arr1 + arr2
arr1.extend(arr2)  # 原地扩展 arr1

# 数组长度
length = len(arr1)      # 元素个数
last_index = len(arr1) - 1  # 最后一个下标

# 哈希表（字典）初步
hash_table = {"name": "Alice", "age": 30}
hash_table["score"] = 95
print(hash_table["name"])

