# -*- coding: utf-8 -*-
# 删除、更新与ALTER语句（ch13 p320）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：pandas（用于表格数据操作）。安装命令：pip install pandas 或 conda install pandas

import pandas as pd

# 创建示例 DataFrame 模拟数据库表
# 表名: table_name，包含 id, column1, old_col 列
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 10],
    'column1': ['a', 'b', 'c', 'd', 'e', 'f'],
    'old_col': [10, 20, 30, 40, 50, 60]
})
print('原始表:')
print(df)

# 条件删除: DELETE FROM table_name WHERE id = 10
df = df[df['id'] != 10]
print('\n删除 id=10 后:')
print(df)

# 更新数据: UPDATE table_name SET column1 = 'updated' WHERE id = 2
df.loc[df['id'] == 2, 'column1'] = 'updated'
print('\n更新 id=2 的 column1 后:')
print(df)

# 修改表结构: ALTER TABLE table_name ADD COLUMN new_col VARCHAR(50)
df['new_col'] = 'default'
print('\n添加 new_col 列后:')
print(df)

# 修改表结构: ALTER TABLE table_name DROP COLUMN old_col
df = df.drop(columns=['old_col'])
print('\n删除 old_col 列后:')
print(df)

# 清空表: TRUNCATE TABLE table_name
df = df.iloc[0:0]
print('\n清空表后:')
print(df)

# 删除表: DROP TABLE table_name
del df
print('\n表已删除（变量已删除）')
