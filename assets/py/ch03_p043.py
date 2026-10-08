# -*- coding: utf-8 -*-
# 相似、同一与同源及直系/旁系同源（ch03 p43）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+
#   无需额外依赖（仅使用标准库）
#   如需可选安装：pip install biopython

# p43: 相似性、同一性与同源性概念检查

def identity_percent(seq1, seq2):
    """计算两条等长序列的同一性百分比。
    注意：同一性(identity)只是序列相似性的一个度量，
    不能直接等同于同源性(homology)。同源性是定性的（有/无），
    不是定量的百分比。
    """
    # 逐位比较，统计相同字符的个数
    same = sum(1 for x, y in zip(seq1, seq2) if x == y)
    # 返回百分比
    return 100.0 * same / len(seq1)

# 示例：两条长度不同的序列，zip 会截断到较短的长度
# 这里 seq1 长度 6，seq2 长度 5，zip 只比较前 5 个字符
print(identity_percent("ACGGTT", "ACGTT"))

# 直系同源(ortholog)与旁系同源(paralog)通常由系统发生树或同源聚类推断，
# 不能仅凭序列同一性百分比直接判定。

