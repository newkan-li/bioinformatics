# -*- coding: utf-8 -*-
# SQL 及数据库编程：数据库与生物数据库（ch13 p312）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：sqlite3（标准库，无需安装）。若需 MySQL 可安装：pip install mysql-connector-python 或 conda install -c conda-forge mysql-connector-python。本示例用 sqlite3 模拟，便于本地运行。

import sqlite3

# 连接内存数据库（模拟 MySQL 的 bioinfo 库）
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# 创建 genes 表
cur.execute('''
CREATE TABLE genes (
    gene_id TEXT PRIMARY KEY,
    gene_name TEXT,
    chromosome TEXT,
    start_pos INTEGER,
    end_pos INTEGER
)
''')

# 插入两条记录
cur.executemany('INSERT INTO genes VALUES (?, ?, ?, ?, ?)', [
    ('G001', 'TP53', '17', 7661779, 7687550),
    ('G002', 'BRCA1', '17', 43044295, 43125483),
])
conn.commit()

# 查询 17 号染色体上的基因
cur.execute("SELECT * FROM genes WHERE chromosome = '17'")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()

