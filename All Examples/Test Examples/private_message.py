# 该代码为发送私密消息的示例代码
import requests
from urllib.parse import quote
import string

# 需要发送的数据包

message='+-* /，。、？：；#$%^&*(@)!“”中文'
message=quote(message)
print(message)
print(message)

data = {
	"fromqq":123456789,
	'toqq':123456789,				# 发送的私密对象ID
	'text':message,	# 发送的消息内容
}

# API接口地址
api_url='http://127.0.0.1:10429/sendprivatemsg'

# 发送数据并接收传回数据
r=requests.post(api_url,data=data)
# 输出传回数据内容
print(r.text)
