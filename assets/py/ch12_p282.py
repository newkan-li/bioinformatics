# -*- coding: utf-8 -*-
# MATLAB Elman神经网络分类实例（ch12 p282）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：numpy, scikit-learn, matplotlib。安装命令：
#   pip install numpy scikit-learn matplotlib
#   或 conda：
#   conda install -c conda-forge numpy scikit-learn matplotlib

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# 1. 构造模拟数据：84 维特征，二分类（外显子/内含子）
# 实际使用时替换为真实特征矩阵 p (84 x N) 和标签 t (1 x N)
np.random.seed(42)
N = 400
p = np.random.randn(84, N)          # 84 维输入，N 个样本
t = np.random.randint(0, 2, N)      # 二分类标签 0/1

# 2. 转置为 sklearn 要求的 (样本数, 特征数)
X = p.T                             # shape = (N, 84)
y = t                               # shape = (N,)

# 3. 划分训练集/测试集：外显子/内含子各随机取 100 个作为独立测试集
# 这里用分层抽样近似“每类各取 100 个”
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=200, stratify=y, random_state=42
)

# 4. 标准化（神经网络对尺度敏感）
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. 构建 Elman 型神经网络（sklearn 用 MLP 近似，单隐层 + tanh + 线性输出）
# hidden_layer_sizes=(51,) 对应 MATLAB 的 51 个隐层神经元
# activation='tanh' 对应 tansig；输出层为线性，用 MLPClassifier 做分类时用 softmax
clf = MLPClassifier(
    hidden_layer_sizes=(51,),
    activation='tanh',
    solver='sgd',
    learning_rate_init=0.01,
    max_iter=3000,
    tol=1e-4,
    random_state=42,
    verbose=False
)

# 6. 训练
clf.fit(X_train, y_train)

# 7. 预测
y_pred = clf.predict(X_test)

# 8. 评估
acc = accuracy_score(y_test, y_pred)
print('Accuracy:', acc)
print(classification_report(y_test, y_pred))

# 9. 时间复杂度说明（注释）
# 单次前向/反向传播约 O(W)，W 为连接权数；
# 训练总复杂度约 O(E * N * W)，E 为迭代次数，N 为样本数。

