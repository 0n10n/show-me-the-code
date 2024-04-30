from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)

# MySQL数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'username',  # 请替换为你的MySQL用户名
    'password': 'password',  # 请替换为你的MySQL密码
    'database': 'abc',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# 获取MySQL连接
connection = pymysql.connect(**db_config)

@app.route('/')
def index():
    try:
        with connection.cursor() as cursor:
            # 执行查询
            sql = "SELECT * FROM users LIMIT 5"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            # 渲染模板，并传递查询结果给模板
            return render_template('user_list.html', users=result)
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
