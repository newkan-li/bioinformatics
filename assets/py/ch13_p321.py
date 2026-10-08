# -*- coding: utf-8 -*-
# PHP特性与安装（ch13 p321）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：pandas（用于模拟数据库查询结果）。安装命令：pip install pandas 或 conda install pandas

import pandas as pd

# 模拟数据库连接和查询
# 创建示例 DataFrame 模拟 journal 表
journal_df = pd.DataFrame({
    'journal_title': ['Nature', 'Science', 'Cell', 'Bioinformatics', 'PLoS ONE'],
    'total_cites': [5000, 4500, 3000, 800, 1200]
})

# 模拟 SQL 查询: SELECT journal_title, total_cites FROM journal WHERE total_cites > 1000
result = journal_df[journal_df['total_cites'] > 1000]

# 模拟 PHP 输出
if len(result) > 0:
    for index, row in result.iterrows():
        print(f"期刊: {row['journal_title']} 引用: {row['total_cites']}")
else:
    print('无结果')
