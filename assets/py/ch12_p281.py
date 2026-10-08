# -*- coding: utf-8 -*-
# 神经网络训练与仿真函数：train、sim、tansig（ch12 p281）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python >= 3.8；依赖：torch, matplotlib。安装命令：pip install torch matplotlib 或 conda install pytorch matplotlib -c pytorch

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

class FFNet(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, out_dim)
        self.act = nn.Tanh()

    def forward(self, x):
        h = self.act(self.fc1(x))
        y = self.fc2(h)
        return y

if __name__ == '__main__':
    torch.manual_seed(0)
    net = FFNet(in_dim=2, hidden_dim=5, out_dim=1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9)

    P = torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
    T = torch.tensor([[0.],[1.],[1.],[0.]])

    for epoch in range(1000):
        optimizer.zero_grad()
        y = net(P)
        loss = criterion(y, T)
        loss.backward()
        optimizer.step()
        if (epoch+1) % 200 == 0:
            print(f'Epoch {epoch+1}, Loss: {loss.item():.6f}')

    with torch.no_grad():
        Y = net(P)
    print('Predictions:')
    print(Y)

    # tansig 激活函数曲线
    x = torch.linspace(-5, 5, 100)
    y = torch.tanh(x)
    plt.plot(x.numpy(), y.numpy())
    plt.grid(True)
    plt.title('tansig (tanh)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('tansig.png')
    plt.show()
