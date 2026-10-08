# -*- coding: utf-8 -*-
# SVM训练算法：块算法与固定工作样本集（ch12 p284）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：numpy, scikit-learn。安装命令：
#   pip install numpy scikit-learn
#   或 conda：
#   conda install numpy scikit-learn

import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. 生成模拟数据
X, y = make_classification(n_samples=200, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. 使用 sklearn 的 SVC 模拟块算法/工作集思想
# sklearn 内部使用 libsvm，采用工作集选择策略（类似 SMO）
clf = SVC(kernel='rbf', C=1.0, gamma='scale', tol=1e-3)
clf.fit(X_train, y_train)

# 3. 获取支持向量、alpha、偏置
support_vectors = clf.support_vectors_
alpha = np.abs(clf.dual_coef_).ravel()   # dual_coef_ 含符号
y_sv = y_train[clf.support_]
b = clf.intercept_[0]

print('支持向量个数:', len(support_vectors))
print('前 5 个 alpha:', alpha[:5])
print('偏置 b:', b)

# 4. 预测
y_pred = clf.predict(X_test)
print('测试集准确率:', accuracy_score(y_test, y_pred))

# 5. 手动实现一个极简块算法演示（仅用于教学，非高效实现）
def simple_chunking_demo(X, y, max_iter=10):
    """极简块算法演示：逐步加入违反 KKT 的样本"""
    n = len(y)
    W = list(range(min(2, n)))  # 初始工作集 W={x1,x2}
    for it in range(max_iter):
        # 在 W 上训练 SVM
        clf_w = SVC(kernel='linear', C=1.0)
        clf_w.fit(X[W], y[W])
        # 计算所有样本的决策值
        decision = clf_w.decision_function(X)
        # 找出违反 KKT 最严重的样本（简化：决策值绝对值最小）
        idx = np.argmin(np.abs(decision))
        if idx not in W:
            W.append(idx)
        # 移除 alpha=0 且非支持向量的样本（简化：保留支持向量）
        sv_idx = clf_w.support_
        W = [i for i in W if i in sv_idx or i == idx]
        if len(W) >= n:
            break
    return W

W_final = simple_chunking_demo(X_train, y_train, max_iter=5)
print('最终工作集大小:', len(W_final))

# 时间复杂度：最坏约 O(n^2) ~ O(n^3)，n 为训练样本数；
# 存储核矩阵在 n>4000 时约需 128 MB。

