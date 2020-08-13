# 聊天机器人主程序

# 导入第三方库
from flask import Flask,request
from json import loads

# 导入程序库
import message_operate
import send_message

# 创建一个服务器对象
bot_server=Flask(__name__)

# 指定服务器对象的API地址及通信模式
@bot_server.route('/api/message',methods=['POST'])

# 定义服务器模块
def server():
	# 初始化
	self_id=3501530063	# 上线用机器人
	#self_id=3522235363	# 测试用机器人

	# 接收消息
	data=request.get_data().decode('utf-8')
	data=loads(data)

	# 避免自我回复
	if data.get("FromQQ").get("UIN")==self_id:
		return ""

	# 处理消息
	message=message_operate.get_message(data)

	# 回复消息，仅当接收到的消息不为空时发送
	if (message!=""):
		send_message.send(self_id,message)

	# 传出空值
	return ""

if __name__=='__main__':
	bot_server.run(port=5701)
