# -*- coding: utf-8 -*-
# Linux命令帮助、文件压缩与打包（ch13 p295）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需第三方包（仅用标准库 subprocess、gzip、bz2、tarfile、os、shutil）。

import subprocess
import gzip
import bz2
import tarfile
import os
import shutil

# 1) 模拟 man ls / help cd：调用系统帮助
def show_help():
    print('=== man ls（前 20 行）===')
    try:
        result = subprocess.run(['man', 'ls'], capture_output=True, text=True, timeout=10)
        print('\n'.join(result.stdout.splitlines()[:20]))
    except Exception as e:
        print('无法调用 man:', e)
    print('\n=== help cd（Python 中无内置 cd，用 os.chdir 说明）===')
    print('os.chdir(path) 用于切换目录，相当于 shell 的 cd')

# 2) 模拟 ls -l：列出当前目录详细信息
def list_long():
    print('\n=== ls -l 等价输出 ===')
    for entry in sorted(os.listdir('.')):
        st = os.stat(entry)
        print(f'{oct(st.st_mode)[-3:]}  {st.st_size:>8}  {entry}')

# 3) gzip 压缩
def gzip_compress(src='file.txt'):
    if not os.path.exists(src):
        with open(src, 'w') as f:
            f.write('hello bioinformatics\n' * 10)
    with open(src, 'rb') as f_in, gzip.open(src + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(f'gzip 压缩完成: {src}.gz')

# 4) bzip2 压缩
def bz2_compress(src='file.txt'):
    with open(src, 'rb') as f_in, bz2.open(src + '.bz2', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(f'bzip2 压缩完成: {src}.bz2')

# 5) tar 打包并 gzip 压缩
def tar_pack(dirname='mydir'):
    os.makedirs(dirname, exist_ok=True)
    with open(os.path.join(dirname, 'a.txt'), 'w') as f:
        f.write('A\n')
    with tarfile.open('archive.tar.gz', 'w:gz') as tar:
        tar.add(dirname, arcname=dirname)
    print('tar 打包完成: archive.tar.gz')

# 6) tar 解包解压
def tar_unpack(archive='archive.tar.gz', dest='unpacked'):
    os.makedirs(dest, exist_ok=True)
    with tarfile.open(archive, 'r:gz') as tar:
        tar.extractall(path=dest)
    print(f'tar 解包完成到: {dest}')

if __name__ == '__main__':
    show_help()
    list_long()
    gzip_compress()
    bz2_compress()
    tar_pack()
    tar_unpack()

