# 该代码为发送群消息的示例代码
import requests
from json import loads

# 需要发送的数据包
data = {
	'group_id':608634144,					# 发送的对象群ID
	'message':'这里是群主开发的聊天机器人，进行发送消息测试中……',		# 发送的消息内容
	'auto_escape':False						# 自动回传
}

# API接口地址
session='http://127.0.0.1:10429/allocsession'

# 发送数据，并接收回传数据
r=requests.post(session).text

# 输出回传数据内容
print(r)

r=loads(r)
session_id=r.get("session_id")
print(session_id)
req={
	"sessid":session_id
}

while True:
	getevent="http://127.0.0.1:10429/getevent"
	data=requests.post(getevent,data=req)
	print(data.text)
