from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

from markupsafe import escape

import uuid
import time
from datetime import datetime

app = Flask(__name__)


def now_time():
    timestamp = time.time()
    visible_time = datetime.fromtimestamp(timestamp)
    return visible_time


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        data = {}
        return render_template('index.html', data=data)
    elif request.method == 'POST':
        data = u"这是一个狗子"
        print(data)
        return jsonify({"status": "success", "data": data})
    else:
        html = f"<p>不支持 {request.method} 请求</p>"
        return html


@app.route('/webhook/create', methods=['POST'])
def create_webhook():
    if request.method == 'POST':
        # username
        username = request.form["username"]
        # key
        key = uuid.uuid4()

        # 与数据库作别对

        # 写入数据库 webhook
        with open("webhook.txt", "w") as file:
            file.write(f"{now_time()}, {key}, {username}")
        data = {
            "username": username,
            "webhook" : f"http://127.0.0.1:5000/webhook?key={key}",
        }
        return render_template('index.html', data=data)
    else:
        return "创建失败"


@app.route('/webhook/send', methods=['POST'])
def send():
    # 获取请求中的key值
    key = request.args.get('key')
    print("key", key)

    data = request.get_json()
    print("收到的数据：", data)

    # 根据 key 找到对应的文件，将收到的数据（追加）存入其中
    file_name = str(key) + '.txt'
    with open(file_name, "a") as file:
        file.write(str(data) + "\n")

    return jsonify({"status": "success"})



if __name__ == '__main__':
    app.run(debug=True)



## 文档

## webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s" % webhook_key
