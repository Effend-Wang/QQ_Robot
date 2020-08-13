# 该代码为发送私密消息的示例代码
import requests

# 需要发送的数据包
data = {
	'user_id':465152177,				# 发送的私密对象ID
	'message':'我是一个可爱的小机器人喵',	# 发送的消息内容
	'auto_escape':False					# 自动回传
}

# API接口地址
api_url='http://127.0.0.1:8080/send_private_msg'

# 发送数据并接收传回数据
r=requests.post(api_url,data=data)
# 输出传回数据内容
print(r.text)
