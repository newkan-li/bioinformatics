# -*- coding: utf-8 -*-
# 字符编辑操作与双序列比对（ch03 p41）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外安装包

def edit_ops(a, b):
    if a == b:
        return ("Match", a, b, 0)
    if a == "-":
        return ("Insert", a, b, 1)
    if b == "-":
        return ("Delete", a, b, 1)
    return ("Replace", a, b, 1)

print(edit_ops("A", "A"))
print(edit_ops("A", "-"))
print(edit_ops("A", "G"))
print(edit_ops("-", "G"))
