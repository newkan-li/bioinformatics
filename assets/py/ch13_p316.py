# -*- coding: utf-8 -*-
# MySQL数据类型、主键与外键（ch13 p316）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：pandas、sqlalchemy、pymysql。安装命令：pip install pandas sqlalchemy pymysql 或 conda install -c conda-forge pandas sqlalchemy pymysql

import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:password@localhost/bioinfo')

# 1) 创建 example 表，包含多种数据类型和键
create_example = '''
CREATE TABLE IF NOT EXISTS example (
  id INT AUTO_INCREMENT PRIMARY KEY,
  created_at DATETIME,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  duration TIME,
  status ENUM('active','inactive','pending'),
  tags SET('bio','info','db')
)
'''
with engine.connect() as conn:
    conn.execute(text(create_example))
    conn.commit()

# 2) 创建 journal 表（若不存在）
create_journal = '''
CREATE TABLE IF NOT EXISTS journal (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
)
'''
with engine.connect() as conn:
    conn.execute(text(create_journal))
    conn.commit()

# 3) 创建 paper 表，带外键
create_paper = '''
CREATE TABLE IF NOT EXISTS paper (
  id INT AUTO_INCREMENT PRIMARY KEY,
  journal_id INT,
  FOREIGN KEY (journal_id) REFERENCES journal(id)
)
'''
with engine.connect() as conn:
    conn.execute(text(create_paper))
    conn.commit()

# 4) 查看表结构
for tbl in ['example', 'journal', 'paper']:
    df = pd.read_sql(text(f'DESCRIBE {tbl}'), engine)
    print(f'\nDESCRIBE {tbl}:')
    print(df)
