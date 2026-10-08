# -*- coding: utf-8 -*-
# 并行计算性能、Amdahl定律、基本方法与云计算（ch13 p326）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：numpy, matplotlib。安装命令：pip install numpy matplotlib 或 conda install -c conda-forge numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

# ===== 1. 性能指标：FLOP/s =====
W = 1e12          # 计算量 workload，单位 FLOP（浮点运算次数）
t = 100.0         # 执行时间 execution_time，单位秒
perf = W / t      # 性能 = 计算量 / 时间，单位 FLOP/s
print(f"Workload W = {W:.2e} FLOP")
print(f"Execution time t = {t} s")
print(f"Performance = {perf:.2e} FLOP/s")

# ===== 2. Amdahl 定律 =====
alpha = 0.10      # 串行比例 serial_fraction（10% 必须串行）
q_values = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

# 加速比 S(q) = 1 / (alpha + (1-alpha)/q)
S = 1.0 / (alpha + (1.0 - alpha) / q_values)

# 理论上界：q -> inf 时 S -> 1/alpha
S_max = 1.0 / alpha
print(f"\nSerial fraction alpha = {alpha}")
print(f"Theoretical upper bound S_max = 1/alpha = {S_max:.2f}")

# 打印每个 q 对应的加速比
for q, s in zip(q_values, S):
    print(f"q = {q:4d}  ->  S = {s:8.4f}")

# ===== 3. 理想并行时间复杂度 O(W/q) =====
# 理想情况下，q 个处理器把计算量 W 均分，每个处理器承担 W/q
# 这里用数组演示：不同 q 下理想时间 t_ideal = t / q
t_ideal = t / q_values
print("\nIdeal parallel time t_ideal = t / q:")
for q, ti in zip(q_values, t_ideal):
    print(f"q = {q:4d}  ->  t_ideal = {ti:.6f} s")

# ===== 4. 可视化 =====
plt.figure(figsize=(8, 5))
plt.plot(q_values, S, 'o-', label='Amdahl speedup S(q)')
plt.axhline(S_max, color='r', linestyle='--', label=f'Upper bound 1/alpha = {S_max:.1f}')
plt.xscale('log', base=2)
plt.xlabel('Number of processors q (log2 scale)')
plt.ylabel('Speedup S')
plt.title(f'Amdahl\'s Law (alpha = {alpha})')
plt.grid(True, which='both', linestyle=':')
plt.legend()
plt.tight_layout()
plt.savefig('amdahl.png', dpi=120)
print("\nPlot saved to amdahl.png")

