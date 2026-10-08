# -*- coding: utf-8 -*-
# 454测序文库制备、乳液PCR与测序步骤（ch14 p332）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需第三方依赖（仅标准库 random）。
#   如需统一环境可用：
#   conda create -n bioinfo python=3.10 -y && conda activate bioinfo
#   pip install biopython numpy pandas matplotlib scipy scikit-learn hmmlearn

import random

def emulsion_pcr_simulation(n_fragments, n_droplets):
    # droplets[i] 表示第 i 个微滴中的模板数量
    droplets = [0] * n_droplets
    # 将每个 DNA 片段随机分配到某个微滴
    for _ in range(n_fragments):
        idx = random.randrange(n_droplets)
        droplets[idx] += 1
    return droplets

if __name__ == "__main__":
    # 固定随机种子，便于复现实验结果
    random.seed(42)
    d = emulsion_pcr_simulation(1000, 100000)
    empty_ratio = d.count(0) / len(d)
    single_ratio = d.count(1) / len(d)
    print("空微滴比例:", empty_ratio)
    print("单模板微滴比例:", single_ratio)

