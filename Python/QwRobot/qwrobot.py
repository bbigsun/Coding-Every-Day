import requests,json,os,logging
# 输出日志到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.INFO)
fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
formatter = logging.Formatter(fmt) 
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
logger.addHandler(console_handler)
class QwRobot:
    def __init__(self,webhook):
        webhook_key = webhook.split('=')[1]
        self.send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s" % webhook_key
        self.upload_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=%s" % webhook_key
    def send_message(self,msgtype="text",message={"content": "Hello World!"}):
        """
        企微机器人发送指定类型消息，默认为 text
        :param msgtype: String 消息类型，默认为 text
        :param message: json 消息内容，默认为 Hello World！
        :return: None
        """
        headers = {'Content-Type': 'application/json'}  # 指定提交的是json
        data = {
            "msgtype": msgtype, 
            msgtype: message
        }
        data = json.dumps(data)
        try:
            res = requests.post(url=self.send_url,data=data,headers=headers,timeout=10)
            res = res.json() # response -> dict
            if res["errcode"] == 0:
                logging.info("errcode: {0}; errmsg: {1}".format(res["errcode"],res["errmsg"]))
            else:
                logging.error("errcode: {0}; errmsg: {1}".format(res["errcode"],res["errmsg"]))
        except Exception as e:
            logging.error("send failed! reason: {}".format(e))
    def send_file(self,filetype,filepath):
        """
        企微机器人快速发送文件
        :param filetype: String 文件类型 (file,voice,image,video)
        :param filepath: String 文件路径
        :return: None
        """
        media_id = self.upload_file(filetype,filepath)
        message = {
            "media_id": media_id
        }
        self.send_message(filetype,message)
    def send_image(self,img_path):
        """
        企微机器人快速发送图片
        :param img_path: String 图片路径，图片大小 2M 以内
        :return: None
        """
        import base64
        import hashlib
        with open(img_path, "rb") as f:
            img_content = f.read() # <class 'bytes'>
            base64_data_md5 = hashlib.md5(img_content).hexdigest() # 通过hashlib库获取MD5值
            base64_data = str(base64.b64encode(img_content),'utf-8') # 获取base64
        message = {
            "base64": base64_data,
            "md5": base64_data_md5
        }
        self.send_message("image",message)
    def upload_file(self,filetype,filepath):
        """
        企微机器人上传文件，三天有效，返回 media_id。
        :param filetype: String 文件类型 (file,voice,image,video)
        :param filepath: String 文件路径
        :return media_id: String 文件标识
        """
        upload_url = self.upload_url + "&type=%s" % filetype
        files = {
            "file": open(filepath, 'rb')
        }
        try:
            res = requests.post(url=upload_url,files=files,timeout=10)
            res = res.json() # response -> dict
            if res["errcode"] == 0:
                logging.info("errcode: {0}; errmsg: {1}".format(res["errcode"],res["errmsg"]))
                return res["media_id"]
            else:
                logging.error("errcode: {0}; errmsg: {1}".format(res["errcode"],res["errmsg"]))
                return None
        except Exception as e:
            logging.error("upload failed! reason: {}".format(e))