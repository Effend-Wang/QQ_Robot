# 该代码为运行flask服务器的示例代码
from flask import Flask,request
from json import loads

# 创建一个服务器对象
bot_server=Flask(__name__)

# 指定服务器对象的API地址及通信模式
@bot_server.route('/api/message',methods=['POST'])

# 定义服务器模块
def server():
	# 使用UTF-8编码处理接收到的数据
	data=request.get_data().decode('utf-8')
	data=loads(data)
	# 输出获得的数据内容
	print(data)

	# 传出数据
	return ''

if __name__=='__main__':
	bot_server.run(port=5701)
