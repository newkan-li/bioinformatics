# -*- coding: utf-8 -*-
# Linux命令提示符、目录结构与文件类型（ch13 p294）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需第三方包（仅用标准库 os、pathlib、platform）。

import os
import platform
from pathlib import Path

# 1) 模拟 pwd：打印当前工作目录
def show_pwd():
    print('当前工作目录:', os.getcwd())
    print('Path.cwd():', Path.cwd())

# 2) 模拟 ls /：列出根目录内容
def list_root():
    root = '/' if platform.system() != 'Windows' else 'C:\\'
    print(f'根目录 {root} 下的内容:')
    try:
        for name in sorted(os.listdir(root)):
            full = os.path.join(root, name)
            kind = '目录' if os.path.isdir(full) else '文件'
            print(f'  {name}  ({kind})')
    except PermissionError:
        print('  权限不足，无法列出全部内容')

# 3) 解释特殊目录
def explain_dirs():
    home = str(Path.home())
    print('~ 表示当前用户主目录:', home)
    print('/ 表示根目录')
    print('/dev 设备文件目录')
    print('/home 用户目录')
    print('/lib 库文件目录')

if __name__ == '__main__':
    show_pwd()
    list_root()
    explain_dirs()

