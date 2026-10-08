# -*- coding: utf-8 -*-
# Ubuntu发行版与Linux常用命令行操作（ch13 p293）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外第三方包（仅用标准库 subprocess、platform、shutil、os）。可选：pip install psutil（用于查看系统信息）。安装命令：pip install psutil

import subprocess
import platform
import shutil
import os

# 1) 查看当前操作系统版本信息（对应 lsb_release -a）
def show_os_release():
    print('=== 操作系统版本信息 ===')
    print('platform.system():', platform.system())
    print('platform.release():', platform.release())
    print('platform.version():', platform.version())
    print('platform.platform():', platform.platform())
    # 在 Linux 上尝试读取 /etc/os-release
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r', encoding='utf-8') as f:
            print(f.read())

# 2) 模拟 apt update：这里只演示如何调用系统命令（需要 sudo 权限，实际运行需谨慎）
def run_command(cmd):
    print(f'>>> 执行命令: {cmd}')
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        print('返回码:', result.returncode)
        if result.stdout:
            print('标准输出:\n', result.stdout[:500])
        if result.stderr:
            print('标准错误:\n', result.stderr[:500])
    except Exception as e:
        print('执行失败:', e)

# 3) 检查 samtools 是否已安装（对应 apt install/remove 的效果检查）
def check_samtools():
    path = shutil.which('samtools')
    if path:
        print('samtools 已安装，路径:', path)
    else:
        print('samtools 未安装（可运行 sudo apt install samtools 安装）')

if __name__ == '__main__':
    show_os_release()
    check_samtools()
    # 下面这行会真正执行 apt update，需要 sudo 权限，默认注释掉
    # run_command('sudo apt update')

