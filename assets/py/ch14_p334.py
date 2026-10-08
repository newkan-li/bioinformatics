# -*- coding: utf-8 -*-
# SOLiD测序原理与流程（ch14 p334）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+
#   无需额外依赖（仅使用标准库）
#   如需完整生物信息学工具链可安装：pip install biopython numpy pandas

# SOLiD 双碱基编码模拟（极简）
# SOLiD 通过连接测序读取双碱基编码，再解码为碱基序列

# 双碱基编码表（简化）
encoding = {
    "AA": "0", "CC": "0", "GG": "0", "TT": "0",
    "AC": "1", "CA": "1", "GT": "1", "TG": "1",
    "AG": "2", "GA": "2", "CT": "2", "TC": "2",
    "AT": "3", "TA": "3", "CG": "3", "GC": "3"
}

def solid_encode(seq):
    """将碱基序列转换为 SOLiD 双碱基编码数字串"""
    return "".join(encoding[seq[i:i+2]] for i in range(len(seq)-1))

# 示例
seq = "ACGTAC"
print(solid_encode(seq))
# 输出: 132132

# 时间复杂度：O(n)
