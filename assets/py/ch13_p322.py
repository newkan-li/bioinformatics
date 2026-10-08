# -*- coding: utf-8 -*-
# 并行计算与高性能计算硬件概述（ch13 p322）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：无（仅使用标准库）。安装命令：无需安装额外包

# 并行计算硬件概述：串行 vs 并行 计算模型

# 定义参数
W = 1000          # 总工作量（例如浮点运算次数）
v_serial = 1.0    # 串行处理速度（单位工作量/秒）
q = 4             # 并行核心数
v_core = 1.0      # 每个核心的处理速度（单位工作量/秒）

# 串行时间：serial_time = W / v_serial
serial_time = W / v_serial
print(f"串行时间: {serial_time} 秒")

# 并行时间：parallel_time = W / (q * v_core)
parallel_time = W / (q * v_core)
print(f"并行时间: {parallel_time} 秒")

# 加速比：speedup = serial_time / parallel_time
speedup = serial_time / parallel_time
print(f"加速比: {speedup}")

# 时间复杂度：O(W) 串行；O(W/q) 理想并行
print(f"串行时间复杂度: O({W})")
print(f"理想并行时间复杂度: O({W}/{q}) = O({W/q})")
