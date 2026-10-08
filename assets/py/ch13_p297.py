# -*- coding: utf-8 -*-
# SAMtools编译安装与Perl简介（ch13 p297）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外第三方包（使用标准库 subprocess、shutil、sys）。若需模拟 Perl 版本检查，可安装 perl（系统包管理器），但 Python 代码本身不依赖 Perl。

import subprocess
import shutil
import sys
from pathlib import Path

# 模拟 SAMtools 编译安装流程（假设源码已解压到 samtools-1.9 目录）
src_dir = Path("samtools-1.9")
if not src_dir.exists():
    print("samtools-1.9 目录不存在，请先运行 p296 的下载解压脚本。")
    sys.exit(1)

# 进入源码目录并执行 configure、make、make install
# 注意：实际安装到 /usr/local 可能需要 sudo 权限，此处仅演示命令调用
commands = [
    ["./configure", "--prefix=/usr/local"],
    ["make"],
    ["make", "install"],
]

for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    # 在 src_dir 目录下执行命令
    result = subprocess.run(cmd, cwd=src_dir, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Command failed: {' '.join(cmd)}")
        print(result.stderr)
        sys.exit(1)

# 验证安装：运行 samtools 查看帮助（如果已安装到 PATH）
print("\nVerifying samtools installation...")
samtools_path = shutil.which("samtools")
if samtools_path:
    result = subprocess.run(["samtools"], capture_output=True, text=True)
    print(result.stdout[:500])  # 只打印前 500 字符
else:
    print("samtools 未在 PATH 中找到，可能未安装或需要重新登录。")

# 模拟 Perl 版本检查与一行代码运行
print("\n===== Perl 简介 =====")
perl_path = shutil.which("perl")
if perl_path:
    # 查看 Perl 版本
    result = subprocess.run(["perl", "-v"], capture_output=True, text=True)
    print(result.stdout)
    # 运行一行 Perl 代码
    result = subprocess.run(["perl", "-e", 'print "Hello, Perl!\n";'], capture_output=True, text=True)
    print(result.stdout)
else:
    print("未找到 perl，请先安装 Perl。")

