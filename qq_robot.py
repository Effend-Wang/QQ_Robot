# 聊天机器人主程序

# 导入第三方库
from flask import Flask,request

# 导入程序库
import message_operate
import send_message
from config_globalvar import config_db_loading
from warframe.warframe_globalvar import warframe_db_loading
from tencent_cloud.tencent_globalvar import tencent_db_loading
import response

# 创建一个服务对象
bot_server=Flask(__name__)

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

	# 处理消息
	message=message_operate.get_message(data)

	# 获得回复消息
	res_msg=response.create(message)

	# 回复消息
	send_message.send(res_msg)

	# 传出空值
	return ""

if __name__=='__main__':
	bot_server.run(port=5701)
