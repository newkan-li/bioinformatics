# -*- coding: utf-8 -*-
# MPI通信函数与简单并行程序示例（ch13 p325）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：mpi4py。安装命令：pip install mpi4py 或 conda install -c conda-forge mpi4py。需要系统安装 MPI 实现（如 OpenMPI 或 MPICH）。

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# 对应 C 示例：打印每个进程的 rank 和总进程数
print(f'{rank}: This is process {rank} out of {size}')

# 可选：同步确保输出顺序
comm.Barrier()

