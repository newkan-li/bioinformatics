# -*- coding: utf-8 -*-
# Python 特点、安装与开发环境（ch13 p309）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；标准库无需额外安装。若需多线程示例，标准库 threading 和 gc 已包含。

import sys
import threading
import gc

# 1. 查看 Python 版本
print("Python version:", sys.version)

# 2. 简单 Python 脚本示例
print("Hello, Bioinformatics!")

# 3. 多线程与垃圾回收示例
def worker(name):
    print("Thread", name, "running")

t = threading.Thread(target=worker, args=("A",))
t.start()
t.join()

gc.collect()
print("Garbage collection done")
