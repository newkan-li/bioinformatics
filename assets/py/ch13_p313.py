# -*- coding: utf-8 -*-
# 表、服务器端脚本语言、SQL、HTML/CSS 与 MySQL 选择理由（ch13 p313）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.9+；依赖：flask（Web 框架）、sqlite3（标准库）。安装：pip install flask 或 conda install -c conda-forge flask。若用 MySQL：pip install flask mysql-connector-python。

from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# 初始化内存数据库并插入数据
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cur = conn.cursor()
    cur.execute('CREATE TABLE genes (gene_id TEXT, gene_name TEXT)')
    cur.executemany('INSERT INTO genes VALUES (?, ?)', [('G001', 'TP53'), ('G002', 'BRCA1')])
    conn.commit()
    return conn

conn = init_db()

HTML = '''
<!doctype html>
<html>
<head><title>Genes</title></head>
<body>
<h1>Gene List</h1>
<table border="1">
<tr><th>Gene ID</th><th>Gene Name</th></tr>
{% for g in genes %}
<tr><td>{{ g[0] }}</td><td>{{ g[1] }}</td></tr>
{% endfor %}
</table>
</body>
</html>
'''

@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute('SELECT gene_id, gene_name FROM genes')
    genes = cur.fetchall()
    return render_template_string(HTML, genes=genes)

if __name__ == '__main__':
    app.run(debug=True)

