# -*- coding: utf-8 -*-
# Perl 正则表达式修饰符、引用与子程序（ch13 p300）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（仅使用标准库）。

# 字符替换（Python 用 str.translate 或 str.replace）
s = 'hello world'
# 转大写
s_upper = s.upper()
print('upper:', s_upper)

# 对非小写字母求补（Perl tr/a-z/A-Z/c 意为将非小写字母替换为大写？实际是补集替换，这里用正则模拟）
import re
s_comp = re.sub(r'[^a-z]', lambda m: m.group().upper(), s)
print('complement upper:', s_comp)

# 删除小写字母
s_del = re.sub(r'[a-z]', '', s)
print('delete lower:', s_del)

# 压缩重复替换字符（Perl tr/a-z/A-Z/s 意为将小写转大写并压缩连续相同字符）
s_squash = re.sub(r'([A-Z])\1+', r'\1', s.upper())
print('squash:', s_squash)

# 引用与反引用（Python 中变量即引用）
array = [1, 2, 3]
aref = array  # 引用
print(aref)

hash_ = {'a': 1}
href = hash_
print(href)

def hello():
    print('hi')

coderef = hello
coderef()
