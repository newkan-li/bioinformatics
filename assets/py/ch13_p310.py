# -*- coding: utf-8 -*-
# Python 交互式运行与反转序列示例及集成开发环境（ch13 p310）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；标准库无需额外安装。

seq = "ATGCGTACGTTAGC"
print(seq)

seqRev = seq[::-1]
print(seqRev)

# 时间复杂度：O(n)，n 为序列长度
