# -*- coding: utf-8 -*-
# phpMyAdmin 管理界面图示（ch13 p314）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：pandas、sqlalchemy、pymysql。安装命令：pip install pandas sqlalchemy pymysql 或 conda install -c conda-forge pandas sqlalchemy pymysql

import pandas as pd
from sqlalchemy import create_engine, text

# 1) 连接 MySQL（请按实际用户名/密码/主机/库名修改）
engine = create_engine('mysql+pymysql://root:password@localhost/bioinfo')

# 2) 查看所有数据库
with engine.connect() as conn:
    dbs = pd.read_sql(text('SHOW DATABASES'), conn)
    print('Databases:')
    print(dbs)

# 3) 查看当前库中的表
tables = pd.read_sql(text('SHOW TABLES'), engine)
print('\nTables in bioinfo:')
print(tables)

# 4) 查看 genes 表结构
desc = pd.read_sql(text('DESCRIBE genes'), engine)
print('\nDESCRIBE genes:')
print(desc)

# 5) 查看服务器状态与版本
status = pd.read_sql(text('SHOW STATUS'), engine)
print('\nServer status (first 5 rows):')
print(status.head())

version = pd.read_sql(text("SHOW VARIABLES LIKE 'version'"), engine)
print('\nMySQL version:')
print(version)

# 6) 导出数据库（用 Python 调用 mysqldump）
import subprocess
with open('bioinfo_backup.sql', 'w') as f:
    subprocess.run(['mysqldump', '-u', 'root', '-ppassword', 'bioinfo'], stdout=f, check=True)
print('\nExported to bioinfo_backup.sql')

# 7) 导入数据库（用 Python 调用 mysql）
with open('bioinfo_backup.sql', 'r') as f:
    subprocess.run(['mysql', '-u', 'root', '-ppassword', 'bioinfo'], stdin=f, check=True)
print('Imported from bioinfo_backup.sql')
