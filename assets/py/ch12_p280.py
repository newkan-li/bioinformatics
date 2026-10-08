# -*- coding: utf-8 -*-
# Elman网络MATLAB函数：newelm、traingdx、learngdm（ch12 p280）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：torch。安装命令：pip install torch 或 conda install pytorch -c pytorch

import torch
import torch.nn as nn
import torch.optim as optim

class ElmanNet(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.fc_in  = nn.Linear(in_dim, hidden_dim)
        self.fc_ctx = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.fc_out = nn.Linear(hidden_dim, out_dim)
        self.act    = nn.Tanh()

    def forward(self, x, h=None):
        if h is None:
            h = torch.zeros(x.size(0), self.hidden_dim)
        h = self.act(self.fc_in(x) + self.fc_ctx(h))
        y = self.fc_out(h)
        return y, h

if __name__ == '__main__':
    torch.manual_seed(0)
    net = ElmanNet(in_dim=2, hidden_dim=8, out_dim=4)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9)  # 类似 learngdm

    # 训练数据：4个样本，每个样本2维输入，4维输出
    P = torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
    T = torch.tensor([[0.,1.,1.,0.],[1.,0.,0.,1.],[1.,0.,0.,1.],[0.,1.,1.,0.]])

    epochs = 1000
    for epoch in range(epochs):
        optimizer.zero_grad()
        y, _ = net(P)
        loss = criterion(y, T)
        loss.backward()
        optimizer.step()
        if (epoch+1) % 200 == 0:
            print(f'Epoch {epoch+1}, Loss: {loss.item():.6f}')

    with torch.no_grad():
        Y, _ = net(P)
    print('Predictions:')
    print(Y)
