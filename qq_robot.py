# 聊天机器人主程序

# 导入第三方库
from flask import Flask,request
import os

# 导入程序库
import message_operate
import send_message
from config_globalvar import config_db_loading
from warframe.warframe_globalvar import warframe_db_loading
from tencent_cloud.tencent_globalvar import tencent_db_loading

# 创建一个服务对象
bot_server=Flask(__name__)

# 定义机器人帐号
self_id_path=os.getcwd()+"/data/config/self_id.txt"
with open(self_id_path) as file:
	self_id=file.read()

# 加载数据库
config_db_loading()
warframe_db_loading()
tencent_db_loading()

# 指定服务对象的API地址及通信模式
@bot_server.route('/api/message',methods=['POST'])

# 定义服务器模块
def server():

	# 接收消息
	data=request.get_data().decode('utf-8')
	data=eval(data)

	# 避免自我回复
	#print(str(data.get("FromQQ").get("UIN"))==self_id)
	if str(data.get("FromQQ").get("UIN"))==self_id:
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
