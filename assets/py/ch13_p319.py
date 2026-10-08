# -*- coding: utf-8 -*-
# 数据插入与SELECT查询（ch13 p319）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；无需第三方包（标准库 sqlite3）。可选：pip install pandas

import sqlite3

conn = sqlite3.connect('bio.db')
cur = conn.cursor()

# 清空并准备 journal 表
cur.execute('DELETE FROM journal')

# 模拟 LOAD DATA：从文本批量插入
rows = [
    ('Cell', '0092-8674', 100000),
    ('Nature', '0028-0836', 90000),
    ('Science', '0036-8075', 95000),
]
cur.executemany('INSERT INTO journal (journal_title, issn, total_cites) VALUES (?,?,?)', rows)
conn.commit()

# 单条插入
cur.execute("INSERT INTO journal (journal_title, issn, total_cites) VALUES (?,?,?)", ('Cell', '0092-8674', 100000))
conn.commit()

# SELECT 查询
cur.execute('SELECT * FROM journal')
print('ALL:', cur.fetchall())

cur.execute("SELECT * FROM journal WHERE journal_title = 'Cell'")
print('WHERE Cell:', cur.fetchall())

cur.execute('SELECT journal_title FROM journal')
print('TITLES:', cur.fetchall())

cur.execute('SELECT journal_title, total_cites FROM journal ORDER BY total_cites DESC LIMIT 10')
print('TOP10:', cur.fetchall())

conn.close()

