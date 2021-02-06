# 消息内容处理接口，分割获得的聊天数据
# 数据分割后包括：
#	接收消息的ID：<data: self_id> <default: "">
# 	聊天类型（私密/群消息）：<data: message_type> <result: "private" & "group"> <default: "">
#	聊天@情况（仅当群消息时获得）：<data: at_status> <result: True & False> <default: "False">
#	聊天@对象（仅当at_status==True时获得）：<data: at_id> <default: []>
#	聊天消息来源群ID（仅当群消息时获得）：<data: req_group> <default: "">
#	聊天消息来源用户ID：<data: req_id> <default: "">
#	聊天消息来源昵称：<data: nickname> <default: "">
#	消息内容：<data: text> <defalut: []>
#	消息图像hash值：<data: pic_hash> <default: []>
#	消息图像guid值：<data: pic_guid> <default: []>
#	语音消息数据：<data: audio> <default: "">

# 私密消息数据的几种情况：
#	1、私密消息
#	2、私密消息+图像信息
#	3、图像信息

# 群消息数据的几种情况：
#	1、群消息
#	2、图像信息
#	3、@成员+群消息
#	4、@成员+群消息+图像信息
#	5、@成员+图像信息
#	6、@成员+无任何消息

import re

# 处理消息全局接口
def get_message(data):

	# 初始化数据默认值
	message={
		"self_id":"",
		"message_type":"",
		"at_status":False,
		"at_id":[],
		"req_group":"",
		"req_id":"",
		"nickname":"",
		"text":"",
		"pic_hash":"",
		"pic_guid":"",
		"audio":""
	}
	
	# 获得全局聊天类型（私密/群消息）
	message_type=data.get("Type")

	# 处理私密消息
	if (message_type=="PrivateMsg"):
		message=private_message(data,message)

	# 处理群消息
	elif (message_type=="GroupMsg"):
		message=group_message(data,message)

	return message

# 私密消息处理
def private_message(data,message):
	message["self_id"]=data.get("LogonQQ")
	message["message_type"]="private"
	message["req_id"]=data.get("FromQQ").get("UIN")
	message["nickname"]=data.get("FromQQ").get("NickName")
	text=data.get("Msg").get("Text")
	if(re.findall(r'(.*)\[pic',text)==[]):
		message["text"]=text
	else:
		message["text"]="".join(re.findall(r'(.*)\[pic',text))
		message["pic_hash"]="".join(re.findall(r'hash=(.*),',text))
		message["pic_guid"]="".join(re.findall(r'guid=(.*)\]',text))

	# Warning: For CoolQ, no longer useful
	#message=""
	#image_url=[]
	#message_length=len(data.get("message"))
	#for i in range(message_length):
		#if(data.get("message")[i].get("type")=="text"):
			#message=message+data.get("message")[i].get("data").get("text")
		#elif(data.get("message")[i].get("type")=="image"):
			#image_url.append(data.get("message")[i].get("data").get("url"))

	return message

# 群消息处理
def group_message(data,message):
	message["self_id"]=data.get("LogonQQ")
	message["message_type"]="group"
	message["req_group"]=data.get("FromGroup").get("GIN")
	message["req_id"]=data.get("FromQQ").get("UIN")
	message["nickname"]=data.get("FromQQ").get("NickName")
	text=data.get("Msg").get("Text")
	if(re.findall(r'(.*)\[pic',text)==[]):
		message["text"]=text
	else:
		message["text"]="".join(re.findall(r'(.*)\[pic',text))
		message["pic_hash"]="".join(re.findall(r'hash=(.*),',text))
		message["pic_guid"]="".join(re.findall(r'guid=(.*)\]',text))

	# Warning: For CoolQ, no longer useful
	#message=""
	#image_url=[]
	#message_length=len(data.get("message"))
	#for i in range(message_length):
		#if(data.get("message")[i].get("type")=="text"):
			#message=message+data.get("message")[i].get("data").get("text")
		#elif(data.get("message")[i].get("type")=="image"):
			#image_url.append(data.get("message")[i].get("data").get("url"))
		#elif(data.get("message")[i].get("type")=="at"):
			#cq_status=True
			#cq_id.append(data.get("message")[i].get("data").get("qq"))
	
	return message
	