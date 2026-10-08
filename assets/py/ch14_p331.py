# -*- coding: utf-8 -*-
# Roche 454测序仪原理与流程（ch14 p331）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需第三方依赖（仅标准库）。
#   如需统一环境可用：
#   conda create -n bioinfo python=3.10 -y && conda activate bioinfo
#   pip install biopython numpy pandas matplotlib scipy scikit-learn hmmlearn

def pyrosequencing_signal(template, flow_order):
    # signals 保存每个 flow 的 (碱基, 连续掺入个数)
    signals = []
    # pos 指向模板中下一个待测位置
    pos = 0
    # 按固定顺序依次“流”入四种 dNTP
    for base in flow_order:
        count = 0
        # 若模板当前位置与当前碱基相同，则连续计数
        while pos < len(template) and template[pos] == base:
            count += 1
            pos += 1
        # 记录本次 flow 的碱基与信号强度（0 表示不发光）
        signals.append((base, count))
    return signals

if __name__ == "__main__":
    template = "AACGGTT"
    flow_order = "ACGT"
    result = pyrosequencing_signal(template, flow_order)
    print(result)

