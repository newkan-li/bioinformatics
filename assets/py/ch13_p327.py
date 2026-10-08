# -*- coding: utf-8 -*-
# 云计算特点、定义及生物信息学应用（ch13 p327）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：无第三方包（仅标准库）。如需可视化可安装 matplotlib：pip install matplotlib 或 conda install -c conda-forge matplotlib

# 云计算特点与生物信息学应用（概念性 Python 演示）

# ===== 1. 用字典描述云计算特点 =====
cloud = {
    'reliability': 'multi-replica + homogeneous nodes',   # 可靠性：多副本 + 同构节点
    'generality': 'multi-tenant, general purpose',         # 通用性：多租户、通用目的
    'scalability': 'dynamic scale in/out',                 # 可扩展性：动态扩缩容
    'on_demand': 'pay-as-you-go (water/electricity model)' # 按需付费：水电模式
}

print("Cloud computing characteristics:")
for key, value in cloud.items():
    print(f"  {key:12s} : {value}")

# ===== 2. 生物信息学典型应用场景 =====
bio_apps = [
    'sequence alignment',   # 序列比对
    'genome assembly',      # 基因组组装
    'variant calling',      # 变异检测
    'RNA-seq quantification',  # 转录组定量
    'phylogenetic analysis'    # 系统发育分析
]

print("\nBioinformatics applications on cloud:")
for i, app in enumerate(bio_apps, 1):
    print(f"  {i}. {app}")

# ===== 3. 按需弹性：模拟峰值负载与动态扩缩容 =====
# 假设任务到达率随时间变化，云平台按 peak_load 动态分配节点
import math

def nodes_needed(load, capacity_per_node=10):
    """根据当前负载计算所需节点数（向上取整）。"""
    return math.ceil(load / capacity_per_node)

# 模拟 12 个时间片的负载（单位：任务数/秒）
loads = [5, 8, 20, 45, 80, 120, 95, 60, 30, 15, 8, 4]

print("\nDynamic scaling simulation (capacity per node = 10 tasks/s):")
print(f"{'time':>4s} {'load':>6s} {'nodes':>6s}")
for t, load in enumerate(loads):
    n = nodes_needed(load)
    print(f"{t:4d} {load:6d} {n:6d}")

peak_load = max(loads)
peak_nodes = nodes_needed(peak_load)
print(f"\nPeak load = {peak_load} tasks/s -> need {peak_nodes} nodes at peak")
print("Cloud scales in/out dynamically: O(peak_load) resources, pay only for what you use.")

