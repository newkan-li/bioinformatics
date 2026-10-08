# -*- coding: utf-8 -*-
# Perl 文件读取与格式化输出总结（ch13 p303）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需第三方包（标准库即可）。

# 逐行读取文件，按制表符分割字段，用 | 连接输出
with open("data.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        line = line.rstrip("\n")          # 去掉换行
        fields = line.split("\t")          # 按制表符分割
        print("|".join(fields))            # 用 | 连接

# 格式化输出（模拟 Perl 的 format/write）
name = "Alice"
score = 95
print(f"{name:<16} {score:>9}")           # 左对齐 16 宽，右对齐 9 宽

# open 三种模式回顾
# "r"  只读
# "w"  重写（覆盖）
# "a"  追加
# with open(...) as fh: 自动 close

