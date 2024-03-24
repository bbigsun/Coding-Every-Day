# Flask

> 欢迎阅读 Flask 的文档。推荐您先从《安装》入手，然后阅读《快速上手》。更详细一些的《教程》介绍 了如何创建一个完整（尽管很小）的 Flask 应用。《Flask 方案》 中介绍了一些常用的解决方案。其余的文档详细介绍了 Flask 的每一个组件。 《API》提供了最详细的参考。

Github 开源地址： https://github.com/pallets/flask

官方文档（英文版）：https://flask.palletsprojects.com/en/3.0.x/

官方文档（中文版）： https://dormousehole.readthedocs.io/en/latest/

Flask 中文网： https://flask.github.net.cn/quickstart.html

## 安装

### Python 版本

推荐使用最新版本的 Python 。 Flask 支持 Python 3.8 以上版本。

### 依赖

当安装 Flask 时，以下配套软件会被自动安装。

- Werkzeug 用于实现 WSGI ，应用和服务之间的标准 Python 接口。
- Jinja 用于渲染页面的模板语言。
- MarkupSafe 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注 入攻击。
- ItsDangerous 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
- Click 是一个命令行应用的框架。用于提供 flask 命令，并允许添加 自定义管理命令。
- Blinker 提供对于 信号 的支持。

### 虚拟环境

建议在开发环境和生产环境下都使用虚拟环境来管理项目的依赖。

为什么要使用虚拟环境？随着你的 Python 项目越来越多，你会发现不同的项目 会需要不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。

虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之 间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。

Python 内置了用于创建虚拟环境的 venv 模块。

#### 创建一个虚拟环境

创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一 个 .venv 文件夹：

macOS/Linux

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
```

Windows

```
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

#### 激活虚拟环境

在开始工作前，先要激活相应的虚拟环境：

macOS/Linux

```
$ . .venv/bin/activate
```

Windows

```
> .venv\Scripts\activate
```

### 安装 Flask

在已激活的虚拟环境中可以使用如下命令安装 Flask：

```
$ pip install Flask
```


## 快速上手


### 一个最小的应用

一个最小的 Flask 应用如下：

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

把它保存为 hello.py 或其他类似名称。请不要使用 flask.py 作为应用名称，这会与 Flask 本身发生冲突。

可以使用 flask 命令或者 python -m flask 来运行这个应 用。你需要使用 --app 选项告诉 Flask 哪里可以找到应用。

运行应用：

```
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

#### 应用发现

作为一个捷径，如果文件名为 app.py 或者 wsgi.py ，那么您不需要使用 --app 。

#### 外部可见服务器

如果您关闭了调试器或信任您网络中的用户，那么可以让服务器被公开访问。 只要在命令行上简单的加上 --host=0.0.0.0 即可:

```
$ flask run --host=0.0.0.0
```

这行代码告诉您的操作系统监听所有公开的 IP 。


### 调试模式

flask run 命令不只可以启动开发服务器。如果您打开调试模式，那么服务器会在修改应用代码之后自动重启，并且当请求过程中发生错误时还会在浏 览器中提供一个交互调试器。

如果要打开调试模式，请使用 --debug 选项。

```
$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

### HTML 转义

当返回 HTML （ Flask 中的默认响应类型）时，为了防止注入攻击，所有用户 提供的值在输出渲染前必须被转义。使用 Jinja （这个稍后会介绍）渲染的 HTML 模板会自动执行此操作。

在下面展示的 escape() 可以手动转义。因为保持简洁的 原因，在多数示例中它被省略了，但您应该始终留心处理不可信的数据。

```
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

如果一个用户想要提交其名称为 `<script>alert("bad")</script>` ，那么 宁可转义为文本，也好过在浏览器中执行脚本。

### 路由

现代 web 应用都使用有意义的 URL ，这样有助于用户记忆，网页会更得到用 户的青睐，提高回头率。

使用 route() 装饰器来把函数绑定到 URL:

```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

```

### 变量规则

通过把 URL 的一部分标记为 `<variable_name>` 就可以在 URL 中添加变量。 标记的部分会作为关键字参数传递给函数。通过使用 `<converter:variable_name>` ，可以选择性的加上一个转换器，为变量指 定规则。请看下面的例子:

```
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

转换器类型：

|  |  |
|--|--|
| string | （缺省值） 接受任何不包含斜杠的文本 |
| int | 接受正整数 |
| float | 接受正浮点数 |
| path | 类似 string ，但可以包含斜杠 |
| uuid | 接受 UUID 字符串 |


### URL 构建

url_for() 函数用于构建指定函数的 URL。它把函数名称作为第 一个参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。 未知变量将添加到 URL 中作为查询参数。

```python
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```
/
/login
/login?next=/
/user/John%20Doe
```

### HTTP 方法

Web 应用使用不同的 HTTP 方法处理 URL 。当您使用 Flask 时，应当熟悉 HTTP 方法。缺省情况下，一个路由只回应 GET 请求。可以使用 route() 装饰器的 methods 参数来处理不同的 HTTP 方法。

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

上例中把路由的所有方法都放在同一个函数中，当每个方法都使用一些共同的 数据时，这样是有用的。

你也可以把不同方法所对应的视图分别放在独立的函数中。 Flask 为每个常用 的 HTTP 方法提供了捷径，如 get() 、 post() 等等。

```python
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
```

如果当前使用了 GET 方法， Flask 会自动添加 HEAD 方法支持，并 且同时还会按照 HTTP RFC 来处理 HEAD 请求。同样， OPTIONS 也会自动实现。


### 静态文件

动态的 web 应用也需要静态文件，一般是 CSS 和 JavaScript 文件。理想情 况下您的服务器已经配置好了为您的提供静态文件的服务。但是在开发过程中， Flask 也能做好这项工作。只要在您的包或模块旁边创建一个名为 static 的文件夹就行了。静态文件位于应用的 /static 中。

使用特定的 'static' 端点就可以生成相应的 URL

```python
url_for('static', filename='style.css')
```

这个静态文件在文件系统中的位置应该是 static/style.css 。

### 渲染模板

在 Python 内部生成 HTML 不好玩，且相当笨拙。因为您必须自己负责 HTML 转义，以确保应用的安全。因此， Flask 自动为您配置 Jinja2 模板引擎。

模板可被用于生成任何类型的文本文件。对于 web 应用来说，主要用于生成 HTML 页面，但是也可以生成 markdown 、用于电子邮件的纯文本等等。

HTML 、 CSS 和其他 web API ，请参阅 MDN Web 文档 。

使用 render_template() 方法可以渲染模板，您只要提供模板 名称和需要作为参数传递给模板的变量就行了。下面是一个简单的模板渲染例 子:

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Flask 会在 templates 文件夹内寻找模板。因此，如果您的应用是一个模块，那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里面：

情形 1 : 一个模块:

```
/application.py
/templates
    /hello.html
```

情形 2 : 一个包:

```
/application
    /__init__.py
    /templates
        /hello.html
```

### 请求对象

从 flask 模块导入请求对象:

```
from flask import request
```

示例：

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

当 form 属性中不存在这个键时会发生什么？会引发一个 KeyError 。如果您不像捕捉一个标准错误一样捕捉 KeyError ， 那么会显示一个 HTTP 400 Bad Request 错误页面。因此，多数情况下您不必 处理这个问题。

要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性:

```python
searchword = request.args.get('key', '')
```

用户可能会改变 URL 导致出现一个 400 请求出错页面，这样降低了用户友好 度。因此，我们推荐使用 get 或通过捕捉 KeyError 来访问 URL 参数。


### 重定向和错误

使用 redirect() 函数可以重定向。使用 abort() 可以更早退出请求，并返回错误代码:

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

缺省情况下每种出错代码都会对应显示一个黑白的出错页面。使用 errorhandler() 装饰器可以定制出错页面:

```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

### 关于响应

视图函数的返回值会自动转换为一个响应对象。如果返回值是一个字符串，那 么会被转换为一个包含作为响应体的字符串、一个 200 OK 出错代码 和一 个 text/html 类型的响应对象。如果返回值是一个字典或者列表， 那么会调用 jsonify() 来产生一个响应。以下是转换的规则：

1. 如果视图返回的是一个响应对象，那么就直接返回它。

2. 如果返回的是一个字符串，那么根据这个字符串和缺省参数生成一个用于 返回的响应对象。

3. 如果返回的是一个迭代器或者生成器，那么返回字符串或者字节，作为流 响应对待。

4. 如果返回的是一个字典或者列表，那么使用 jsonify() 创建一个响应对象。

5. 如果返回的是一个元组，那么元组中的项目可以提供额外的信息。元组中 必须至少包含一个项目，且项目应当由 (response, status) 、 (response, headers) 或者 (response, status, headers) 组 成。 status 的值会重载状态代码， headers 是一个由额外头部 值组成的列表或字典。

6. 如果以上都不是，那么 Flask 会假定返回值是一个有效的 WSGI 应用并把 它转换为一个响应对象。


### JSON 格式 API


JSON 格式的响应是常见的，用 Flask 写这样的 API 是很容易上手的。如果从 视图返回一个 dict 或者 list ，那么它会被转换为一个 JSON 响应。

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
```

如果 dict 还不能满足需求，还需要创建其他类型的 JSON 格式响应，可以使用 jsonify() 函数。该函数会序列化任何支持的 JSON 数据类型。

## 教程


## Flask 方案


## API 参考

API 文档： https://dormousehole.readthedocs.io/en/latest/api.html