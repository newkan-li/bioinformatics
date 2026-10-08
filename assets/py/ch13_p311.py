# -*- coding: utf-8 -*-
# Python 生物信息常用程序与 R 语言简介（ch13 p311）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：matplotlib。安装命令：pip install matplotlib 或 conda install -c conda-forge matplotlib。PyMOL 为可选外部工具，安装：conda install -c schrodinger pymol-bundle（或系统包管理器）。

import matplotlib
matplotlib.use('Agg')  # 使用非交互后端，便于脚本保存图片
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  # 样本编号
y = [2, 4, 1, 5, 3]  # 对应数值

plt.plot(x, y, marker='o')  # 折线图，数据点用圆点标记
plt.xlabel('Sample')  # x 轴标签
plt.ylabel('Value')  # y 轴标签
plt.title('Bioinformatics Data')  # 图标题
plt.savefig('plot.png', dpi=300)  # 保存为高分辨率 PNG
plt.show()  # 显示图形（在 Agg 后端下无窗口，仅占位）

# PyMOL 命令行示例（需先安装 PyMOL，本脚本不执行）
# 终端运行：pymol protein.pdb
# 在 PyMOL 交互界面中执行：
# show cartoon
# color blue, chain A
# png structure.png, width=800, height=600, dpi=300

