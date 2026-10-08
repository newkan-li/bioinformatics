# -*- coding: utf-8 -*-
# Perl 随机数、排序、反转与文件处理（ch13 p302）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外第三方包（标准库 random 即可）。如需可复现实验可安装 numpy：pip install numpy

import random

# 随机数：生成 -50 到 +50 之间的浮点数
r = random.uniform(-50, 50)  # 等价于 Perl 的 rand(100)-50
print(f"random r = {r:.4f}")

# reverse 与 sort
arr = [3, 1, 4, 1, 5]
rev = list(reversed(arr))          # 反转列表
sorted_arr = sorted(arr)           # 升序排序
print("arr       =", arr)
print("reversed  =", rev)
print("sorted    =", sorted_arr)

# 文件处理：逐行读取并打印
file = "data.txt"
try:
    with open(file, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")   # 去掉行尾换行，类似 chomp
            print(line)
except FileNotFoundError:
    print(f"Cannot open {file}")

# 写入文件（覆盖）
with open("out.txt", "w", encoding="utf-8") as out:
    out.write("Hello\n")

# 追加写入
with open("out.txt", "a", encoding="utf-8") as app:
    app.write("World\n")

# 验证写入结果
with open("out.txt", "r", encoding="utf-8") as f:
    print("--- out.txt ---")
    print(f.read(), end="")

