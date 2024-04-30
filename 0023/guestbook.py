
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 初始留言列表
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    # 从表单获取用户输入的留言内容
    message = request.form['message']
    
    # 将留言添加到留言列表中
    messages.append(message)
    
    # 重定向到首页
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
