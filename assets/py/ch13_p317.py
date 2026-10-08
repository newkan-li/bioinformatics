# -*- coding: utf-8 -*-
# 数据库设计与范式（ch13 p317）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；无需第三方包（仅用标准库 sqlite3）。如需可选依赖：pip install pandas

import sqlite3

# 使用内存数据库演示 1NF -> 2NF -> 3NF 的规范化过程
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# ---------- 1NF：非规范化表（存在重复列/非原子值风险） ----------
cur.executescript('''
CREATE TABLE student_1nf (
    id INTEGER,
    name TEXT,
    course TEXT,
    zip TEXT,
    city TEXT
);
INSERT INTO student_1nf VALUES
 (1,'Alice','Math','10001','Beijing'),
 (1,'Alice','Bio','10001','Beijing'),
 (2,'Bob','Math','20002','Shanghai');
''')

# ---------- 2NF：拆分复合主键带来的部分依赖 ----------
cur.executescript('''
CREATE TABLE student_2nf (
    id INTEGER PRIMARY KEY,
    name TEXT,
    zip TEXT,
    city TEXT
);
CREATE TABLE course_2nf (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
);
CREATE TABLE student_course_2nf (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student_2nf(id),
    FOREIGN KEY (course_id) REFERENCES course_2nf(course_id)
);
INSERT INTO student_2nf VALUES (1,'Alice','10001','Beijing'),(2,'Bob','20002','Shanghai');
INSERT INTO course_2nf VALUES (1,'Math'),(2,'Bio');
INSERT INTO student_course_2nf VALUES (1,1),(1,2),(2,1);
''')

# ---------- 3NF：消除 zip -> city 的传递依赖 ----------
cur.executescript('''
CREATE TABLE student_3nf (
    id INTEGER PRIMARY KEY,
    name TEXT,
    zip TEXT,
    FOREIGN KEY (zip) REFERENCES zip_city_3nf(zip)
);
CREATE TABLE zip_city_3nf (
    zip TEXT PRIMARY KEY,
    city TEXT
);
INSERT INTO zip_city_3nf VALUES ('10001','Beijing'),('20002','Shanghai');
INSERT INTO student_3nf VALUES (1,'Alice','10001'),(2,'Bob','20002');
''')

# 验证：查询 3NF 结果
cur.execute('SELECT s.id, s.name, z.city FROM student_3nf s JOIN zip_city_3nf z ON s.zip=z.zip')
for row in cur.fetchall():
    print(row)

conn.close()

