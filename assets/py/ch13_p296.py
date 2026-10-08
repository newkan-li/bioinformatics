# -*- coding: utf-8 -*-
# SAMtools源码下载与解压示例（ch13 p296）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外第三方包（仅使用标准库 urllib、tarfile、pathlib）。若需更稳健下载可安装 requests：pip install requests

import urllib.request
import tarfile
from pathlib import Path

# 定义要下载的 SAMtools 与 HTSlib 源码包 URL
urls = {
    "samtools-1.9.tar.bz2": "https://nchc.dl.sourceforge.net/project/samtools/samtools/1.9/samtools-1.9.tar.bz2",
    "htslib-1.9.tar.bz2": "https://nchc.dl.sourceforge.net/project/htslib/htslib/1.9/htslib-1.9.tar.bz2",
}

# 下载每个文件到当前目录
for filename, url in urls.items():
    print(f"Downloading {filename} ...")
    urllib.request.urlretrieve(url, filename)  # 下载并保存为本地文件
    print(f"Saved {filename}")

# 解压 .tar.bz2 文件
for filename in urls:
    print(f"Extracting {filename} ...")
    with tarfile.open(filename, "r:bz2") as tar:  # 以 bz2 压缩格式打开 tar 包
        tar.extractall()  # 解压到当前目录
    print(f"Extracted {filename}")

# 查看 samtools-1.9/README 内容（模拟 cat 命令）
readme = Path("samtools-1.9/README")
if readme.exists():
    print("\n===== samtools-1.9/README =====")
    print(readme.read_text(errors="ignore"))  # 读取并打印 README 文本
else:
    print("README not found, extraction may have failed.")

