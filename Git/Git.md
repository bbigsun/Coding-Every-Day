# Git

官网地址： https://git-scm.com/

官方文档： https://git-scm.com/doc

官方中文文档已下载至本地见文件：progit.pdf

官方下载地址： https://git-scm.com/downloads

支持平台： Linux, macOS 以及 Windows


## GitHub

### 脚本 GitHub

GitHub 开发者文档： https://docs.github.com/cn/developers/webhooks-and-events/webhooks/about-webhooks 

如果需要做一些更具体的事，或者想要整合一个不在这个列表中的服务或站点，可以转而使用更通用的钩子系统。 GitHub 仓库钩子是非常简单的。 指定一个 URL 然后 GitHub 在任一期望的事件发生时就会发送一个 HTTP 请求到那个 URL 。

通常做这件事的方式是可以设置一个小的 web 服务来监听 GitHub 钩子请求然后使用收到的数据做一些事情。

1、GitHub 设置一个钩子（Add webhook）

2、设置一个 web 服务监听 GitHub 钩子

假设我们想要在某个特定的人推送到我们的项目的特定分支并修改一个特定文件时得到一封邮件。

```ruby
require 'sinatra'
require 'json'
require 'mail'

post '/payload' do
  push = JSON.parse(request.body.read) # parse the JSON

  # gather the data we're looking for
  pusher = push["pusher"]["name"]
  branch = push["ref"]

  # get a list of all the files touched
  files = push["commits"].map do |commit|
    commit['added'] + commit['modified'] + commit['removed']
  end
  files = files.flatten.uniq

  # check for our criteria
  if pusher == 'schacon' &&
     branch == 'ref/heads/special-branch' &&
     files.include?('special-file.txt')

    Mail.deliver do
      from     'tchacon@example.com'
      to       'tchacon@example.com'
      subject  'Scott Changed the File'
      body     "ALARM"
    end
  end
end
```

```python
import json
import smtplib
from email.mime.text import MIMEText

def send_email():
    from_email = 'tchacon@example.com'
    to_email = 'tchacon@example.com'
    subject = 'Scott Changed the File'
    body = 'ALARM'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, [to_email], msg.as_string())
    server.quit()

def handle_payload(request):
    push = json.loads(request.data)

    pusher = push["pusher"]["name"]
    branch = push["ref"]

    files = []
    for commit in push["commits"]:
        files += commit['added'] + commit['modified'] + commit['removed']
    files = list(set(files))

    if pusher == 'schacon' and branch == 'ref/heads/special-branch' and 'special-file.txt' in files:
        send_email()

```

