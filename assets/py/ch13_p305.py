# -*- coding: utf-8 -*-
# Perl DBI 数据库操作与结果集获取（ch13 p305）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：sqlite3（标准库，无需安装）。如需 MySQL 可安装：pip install mysql-connector-python 或 conda install -c conda-forge mysql-connector-python。本示例用 sqlite3 演示，无需额外安装。

import sqlite3

# 连接数据库（内存数据库，便于演示）
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# 建表并插入测试数据
cur.execute('CREATE TABLE sequences (id INTEGER PRIMARY KEY, name TEXT, seq TEXT)')
cur.executemany('INSERT INTO sequences (name, seq) VALUES (?, ?)', [
    ('geneA', 'ATGC' * 30),
    ('geneB', 'ATGC' * 10),
    ('geneC', 'ATGC' * 50),
])
conn.commit()

# 1. prepare + execute 查询（参数化查询）
cur.execute('SELECT id, name, seq FROM sequences WHERE length(seq) > ?', (100,))

# 2. fetchone / 迭代：逐行获取
print('--- 逐行获取 ---')
for row in cur:
    print('\t'.join(str(x) for x in row))

# 3. fetchall：返回整个结果集
cur.execute('SELECT id, name FROM sequences')
all_rows = cur.fetchall()
print('--- fetchall ---')
for row in all_rows:
    print('\t'.join(str(x) for x in row))

# 4. 使用 pandas 读取结果集（可选）
try:
    import pandas as pd
    df = pd.read_sql_query('SELECT id, name FROM sequences', conn)
    print('--- pandas DataFrame ---')
    print(df)
except ImportError:
    print('pandas 未安装，跳过 DataFrame 演示')

# 5. execute 执行 insert / update / delete
cur.execute('INSERT INTO sequences (name, seq) VALUES (?, ?)', ('gene1', 'ATGC'))
rows_inserted = cur.rowcount
cur.execute('UPDATE sequences SET seq = ? WHERE name = ?', ('ATGCGT', 'gene1'))
rows_updated = cur.rowcount
cur.execute('DELETE FROM sequences WHERE name = ?', ('gene1',))
rows_deleted = cur.rowcount
conn.commit()
print(f'inserted={rows_inserted}, updated={rows_updated}, deleted={rows_deleted}')

conn.close()

