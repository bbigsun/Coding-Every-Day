import requests

# get 请求
def get():
    url = "http://127.0.0.1:5000/webhook/create"  # 替换为您的Webhook URL

    response = requests.get(url)

    print(response.status_code)
    print(response.text)


# post 请求
def post():
    url = "http://127.0.0.1:5000/webhook/send?key=6ce4c8ba-befc-4ac5-b067-dedc6d51d1c6"  # 替换为您的Webhook URL
    data = {
        "key1": "value1",
        "key2": "value2"
    }

    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    post()
