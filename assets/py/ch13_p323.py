# -*- coding: utf-8 -*-
# 集群体系结构及其在生物信息学中的应用（ch13 p323）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：无第三方包（仅标准库）。可选安装：pip install numpy matplotlib（用于可视化节点/网络示意）。

import math

class Node:
    def __init__(self, cpu, mem):
        self.cpu = cpu
        self.mem = mem

    def __repr__(self):
        return f"Node(cpu={self.cpu}, mem={self.mem})"

N = 4  # 节点数量
cluster = {
    'nodes': [Node(cpu=8, mem=32) for _ in range(N)],
    'network': 'Ethernet / InfiniBand',
    'storage': 'shared FS (NFS/Lustre)',
    'ups': True,
    'cooling': True
}

print('Cluster nodes:', cluster['nodes'])
print('Network:', cluster['network'])
print('Storage:', cluster['storage'])
print('UPS:', cluster['ups'], 'Cooling:', cluster['cooling'])

# 通信开销示意：O(log N) ~ O(N)
log_cost = math.log2(N) if N > 0 else 0
linear_cost = N
print(f'Communication cost: O(log N) ~ {log_cost:.2f}, O(N) ~ {linear_cost}')
print('Top500 cluster share ~ 85%')

