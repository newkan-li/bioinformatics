# -*- coding: utf-8 -*-
# Illumina/Solexa测序原理与流程（ch14 p333）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需第三方依赖（仅标准库）。
#   如需统一环境可用：
#   conda create -n bioinfo python=3.10 -y && conda activate bioinfo
#   pip install biopython numpy pandas matplotlib scipy scikit-learn hmmlearn

def illumina_sequencing(read, cycles):
    # result 保存每轮读取到的碱基
    result = []
    # 最多测 cycles 轮，且不超过 read 长度
    for i in range(min(cycles, len(read))):
        base = read[i]
        # 模拟荧光标记 dNTP 掺入并成像，读取当前碱基
        result.append(base)
    return "".join(result)

if __name__ == "__main__":
    read = "ACGTACGT"
    cycles = 8
    seq = illumina_sequencing(read, cycles)
    print(seq)

