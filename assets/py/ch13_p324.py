# -*- coding: utf-8 -*-
# 消息传递与MPI基本函数（ch13 p324）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；依赖：mpi4py。安装命令：pip install mpi4py 或 conda install -c conda-forge mpi4py。需要系统安装 MPI 实现（如 OpenMPI 或 MPICH）。

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# 发送进程：rank 0 发送数据给 rank 1
if rank == 0:
    send_buffer = [1, 2, 3, 4, 5]
    print(f'Rank {rank}: sending {send_buffer} to rank 1')
    comm.send(send_buffer, dest=1, tag=11)

# 接收进程：rank 1 接收数据
if rank == 1:
    recv_buffer = comm.recv(source=0, tag=11)
    print(f'Rank {rank}: received {recv_buffer} from rank 0')

# 同步机制：barrier 确保所有进程到达此处
comm.Barrier()
print(f'Rank {rank}: passed barrier')

