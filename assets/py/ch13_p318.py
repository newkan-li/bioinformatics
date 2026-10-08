# -*- coding: utf-8 -*-
# 创建表与查询数据库信息（ch13 p318）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；无需第三方包（标准库 sqlite3）。可选：pip install pandas

import sqlite3

conn = sqlite3.connect('bio.db')  # 持久化数据库文件
cur = conn.cursor()

# 创建 journal 表
cur.execute('''
CREATE TABLE IF NOT EXISTS journal (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  journal_title VARCHAR(50),
  issn VARCHAR(20),
  total_cites INTEGER
)
''')

# 创建 paper 表，含外键
cur.execute('''
CREATE TABLE IF NOT EXISTS paper (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(200),
  journal_id INTEGER,
  FOREIGN KEY (journal_id) REFERENCES journal(id)
)
''')
conn.commit()

# 查询数据库信息
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('TABLES:', cur.fetchall())

cur.execute("PRAGMA table_info(journal)")
print('JOURNAL COLUMNS:', cur.fetchall())

cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='paper'")
print('PAPER DDL:', cur.fetchone()[0])

conn.close()

