# 该代码为发送群消息的示例代码
import requests

# 需要发送的数据包
data = {
	'group_id':123456789,					# 发送的对象群ID
	'message':'这里是群主开发的聊天机器人，进行发送消息测试中……',		# 发送的消息内容
	'auto_escape':False						# 自动回传
}

# API接口地址
api_url='http://127.0.0.1:8080/send_group_msg'

# 发送数据，并接收回传数据
r=requests.post(api_url,data=data)

# 输出回传数据内容
print(r.text)
