# -*- coding: utf-8 -*-
# 期刊影响因子表示例与 MySQL 列类型引入（ch13 p315）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：pandas、sqlalchemy、pymysql。安装命令：pip install pandas sqlalchemy pymysql 或 conda install -c conda-forge pandas sqlalchemy pymysql

import pandas as pd
from sqlalchemy import create_engine, text

# 连接 MySQL（请修改用户名密码）
engine = create_engine('mysql+pymysql://root:password@localhost/bioinfo')

# 1) 创建表 journal_impact
create_sql = '''
CREATE TABLE IF NOT EXISTS journal_impact (
    abbrev_title VARCHAR(100),
    issn VARCHAR(20),
    total_cites INT,
    impact_factor DECIMAL(6,3)
)
'''
with engine.connect() as conn:
    conn.execute(text(create_sql))
    conn.commit()

# 2) 插入数据
insert_sql = '''
INSERT INTO journal_impact VALUES
('CANCER CELL', '1535-6108', 17941, 26.925),
('MOL CELL', '1097-2765', 42991, 14.194),
('ANNU REV', '1543-5008', 12000, 10.500)
'''
with engine.connect() as conn:
    conn.execute(text(insert_sql))
    conn.commit()

# 3) 查询并按影响因子降序排列
df = pd.read_sql(text('SELECT abbrev_title, impact_factor FROM journal_impact ORDER BY impact_factor DESC'), engine)
print(df)
