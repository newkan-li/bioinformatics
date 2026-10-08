# -*- coding: utf-8 -*-
# 单细胞测序应用与宏基因组学（ch14 p345）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：scanpy, anndata, numpy, pandas, matplotlib, leidenalg。安装命令：
#   pip install scanpy anndata numpy pandas matplotlib leidenalg
#   或 conda：
#   conda install -c conda-forge scanpy anndata numpy pandas matplotlib leidenalg

import scanpy as sc
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 设置日志
sc.settings.verbosity = 3
sc.settings.set_figure_params(dpi=80, facecolor='white')

# 1. 读取 10x 矩阵
# 真实数据路径：filtered_feature_bc_matrix/
# 这里用 scanpy 内置数据集模拟
adata = sc.datasets.pbmc3k()
print(f"原始数据: {adata.n_obs} 细胞 x {adata.n_vars} 基因")

# 2. 过滤细胞
sc.pp.filter_cells(adata, min_genes=200)
print(f"过滤后: {adata.n_obs} 细胞")

# 3. 归一化
sc.pp.normalize_total(adata, target_sum=1e4)

# 4. 对数变换
sc.pp.log1p(adata)

# 5. 高变基因
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
print(f"高变基因数: {adata.var['highly_variable'].sum()}")

# 6. PCA
sc.tl.pca(adata)
print(f"PCA 完成，主成分数: {adata.obsm['X_pca'].shape[1]}")

# 7. 邻居图
sc.pp.neighbors(adata)

# 8. UMAP
sc.tl.umap(adata)

# 9. Leiden 聚类
sc.tl.leiden(adata)
print(f"聚类数: {adata.obs['leiden'].nunique()}")

# 10. 保存 UMAP 图
sc.pl.umap(adata, color='leiden', show=False)
plt.savefig('umap_leiden.png', dpi=100)
print("已保存 umap_leiden.png")

# 应用说明
print("应用: CAR-T 免疫反应、肿瘤异质性、CTC、早期胚胎")
print("时间复杂度: PCA O(N*D^2)，UMAP O(N log N)")
