# -*- coding: utf-8 -*-
# 动态神经网络概述与Elman网络（ch12 p279）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：torch。安装命令：pip install torch 或 conda install pytorch -c pytorch

import torch
import torch.nn as nn

class ElmanNet(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.fc_in  = nn.Linear(in_dim, hidden_dim)          # 输入到隐层
        self.fc_ctx = nn.Linear(hidden_dim, hidden_dim, bias=False)  # 上下文(上一时刻隐层)到隐层
        self.fc_out = nn.Linear(hidden_dim, out_dim)         # 隐层到输出
        self.act    = nn.Tanh()                              # 激活函数

    def forward(self, x, h=None):
        # x: (batch, in_dim); h: (batch, hidden_dim)
        if h is None:
            h = torch.zeros(x.size(0), self.hidden_dim)      # 初始隐状态为0
        h = self.act(self.fc_in(x) + self.fc_ctx(h))         # 更新隐状态
        y = self.fc_out(h)                                   # 计算输出
        return y, h

if __name__ == '__main__':
    torch.manual_seed(0)
    net = ElmanNet(in_dim=3, hidden_dim=4, out_dim=2)
    x = torch.randn(1, 3)                                    # 一个样本
    y, h = net(x)
    print('y =', y)
    print('h =', h)
    # 时间步序列演示
    seq = torch.randn(5, 1, 3)                               # 5个时间步
    h = None
    for t in range(seq.size(0)):
        y, h = net(seq[t], h)
        print(f't={t}, y={y.detach().numpy()}, h={h.detach().numpy()}')
