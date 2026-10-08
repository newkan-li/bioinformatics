# -*- coding: utf-8 -*-
# Perl 文件读取与模块使用（ch13 p304）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；Web 访问需安装 requests：pip install requests（或 conda install requests）。标准库无需额外安装。

import os

# 准备示例文件
with open("input.txt", "w", encoding="utf-8") as f:
    f.write("line1\nline2\nline3\n")

# 1. read 函数：按字节读取
with open("input.txt", "rb") as fh:
    while True:
        buf = fh.read(1)          # 每次读 1 字节
        if not buf:
            break
        print(buf.decode("utf-8"), end="")
print()

# 2. readline / 逐行读取
with open("input.txt", "r", encoding="utf-8") as fh2:
    for line in fh2:
        print(line, end="")
print()

# 3. getc 读取单个字符
with open("input.txt", "r", encoding="utf-8") as fh3:
    while True:
        ch = fh3.read(1)          # 读 1 个字符
        if not ch:
            break
        print(ch, end="")
print()

# 4. eof 测试文件尾
with open("input.txt", "r", encoding="utf-8") as fh4:
    while True:
        line = fh4.readline()
        if line == "":            # 空字符串表示 EOF
            break
        print(line, end="")
print()

# 5. 统计文件行数
with open("input.txt", "r", encoding="utf-8") as fh5:
    count = sum(1 for _ in fh5)
print(f"Lines: {count}")

# 6. requests 访问 Web 页面（替代 LWP::Simple）
try:
    import requests
    content = requests.get("http://www.example.com/", timeout=10).text
    print(content[:200])          # 只打印前 200 字符
    # 7. 带状态检查的访问（替代 LWP::UserAgent）
    resp = requests.get("http://www.example.com/", timeout=10)
    if resp.ok:
        print(resp.text[:200])
    else:
        print(f"HTTP error: {resp.status_code}")
except ImportError:
    print("requests 未安装，跳过 Web 示例")
except Exception as e:
    print(f"Web 访问失败: {e}")

# 时间复杂度：逐行/逐字节读取 O(n)，n 为文件大小

