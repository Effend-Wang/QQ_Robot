# 消息内容处理接口，分割获得的聊天数据
# 数据分割后包括：
# 	聊天类型（私密/群消息）：<data: message_type> <result: "private" & "group">
#	聊天@情况（仅当群消息时获得）：<data: cq_status> <result: True & False> <default: "False">
#	聊天@对象（仅当cq_status==True时获得）：<data: cq_id> <default: []>
#	聊天消息来源群ID（仅当群消息时获得）：<data: group_id> <default:"">
#	聊天消息来源用户ID：<data: user_id>
#	聊天消息来源昵称：<data: nickname>
#	消息内容：<data: message> <defalut:"">
#	消息图像URL（当存在消息type=="image"时）：<data: image_url> <default: []>
#	消息处理状态：<data: message_status> <result: True & False> <default: True>

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

# 处理消息全局接口
def get_message(data):

	# 初始化数据默认值
	message_type=""
	at_status=False
	at_id=[]
	group_id=""
	user_id=""
	nickname=""
	message=""
	image_url=[]
	message_status=False
	
	# 获得全局聊天类型（私密/群消息）
	message_type=data.get("Type")

	# 处理私密消息
	if (message_type=="PrivateMsg"):
		message_type="private"
		(user_id,nickname,message,image_url,message_status)=private_message(data)

	# 处理群消息
	elif (message_type=="GroupMsg"):
		message_type="group"
		(at_status,at_id,group_id,user_id,nickname,message,image_url,message_status)=group_message(data)

	# 输出消息
	#print("收到一条%s消息：" %message_type)
	#print("@类型：%s\t@对象：%s" %(at_status,at_id))
	#print("来自QQ：%s\t昵称：%s" %(user_id,nickname))
	#print("消息类型：%s" %message_type)
	#print("消息内容：%s" %message)
	#print("消息图像URL：%s" %image_url)
	#print("消息处理状态：%s\n" %message_status)

	# 整合数据
	message={
		"message_type":message_type,
		"at_status":at_status,
		"at_id":at_id,
		"group_id":group_id,
		"user_id":user_id,
		"nickname":nickname,
		"message":message,
		"image_url":image_url,
		"message_status":message_status
	}

	return message

# 私密消息处理
def private_message(data):
	image_url=""
	user_id=data.get("FromQQ").get("UIN")
	nickname=data.get("FromQQ").get("NickName")
	message=data.get("Msg").get("Text")

	# Warning: For CoolQ, no longer useful
	#message=""
	#image_url=[]
	#message_length=len(data.get("message"))
	#for i in range(message_length):
		#if(data.get("message")[i].get("type")=="text"):
			#message=message+data.get("message")[i].get("data").get("text")
		#elif(data.get("message")[i].get("type")=="image"):
			#image_url.append(data.get("message")[i].get("data").get("url"))

	if message!="":
		message_status=True
	else:
		message_status=False
	
	return user_id,nickname,message,image_url,message_status

# 群消息处理
def group_message(data):
	at_status=False
	at_id=[]
	image_url=""
	group_id=data.get("FromGroup").get("GIN")
	user_id=data.get("FromQQ").get("UIN")
	nickname=data.get("FromQQ").get("Card")
	message=data.get("Msg").get("Text")

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

	if message!="":
		message_status=True
	else:
		message_status=False
	
	return at_status,at_id,group_id,user_id,nickname,message,image_url,message_status
	