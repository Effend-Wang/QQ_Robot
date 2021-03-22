'''

该模块用于创建回复内容
流程：初始化回复内容 --> 对请求消息鉴权 --> 从各功能模块中获取消息 --> 返回回复内容

模块需要传入message_operate.get_message的返回值，即将请求信息处理后的内容
模块返回需要发送的消息内容

回复数据类型为字典，内容有：
	message_type："private"或"group"。用于判断为私聊消息或群消息
	fromqq：发送回复的机器人qq号
	toqq：回复对象的qq号（仅在私聊消息时用）
	togroup：回复对象的群号（仅在群消息时用）
	anonymous：是否匿名发送（仅在群消息时用）（此参数实际无需使用）
	have_text：布尔值，用于判断是否有需要回复的文字消息
	text：回复的文字消息内容
	have_pic：布尔值，用于判断是否有需要回复的图片消息
	pic_type：需提供给框架的发送图片信息的类型
	pic_line：当pic_type=0时，图片的上传信息，该信息格式为[pic,hash=<hashvalue>,gui=<guidevalue>]
	pic_path：当pic_type=1时，图片的本地绝对路径
	pic_url：当pic_type=2时，图片的网络链接地址
	have_audio：布尔值，用于判断是否有需要回复的语音信息
	audio_type：需提供给框架的发送语音信息的类型
	audio_line：当audio_type=0时，语音的上传信息，格式暂时未知
	audio_path：当audio_type=1时，语音的本地绝对路径
	audio_url：当audio_type=2时，语音的网络链接地址

'''

# 导入程序库
from chat_authority import get_authority
from warframe.warframe_operate import warframe
from admin.admin_operate import admin
from tencent_cloud.tencent_operate import tencent
from webcrawler.crawler_operate import crawler
from tools.word2pic import w2p
from game.game_operate import game
from honkai3.honkai3_operate import honkai3
from manage.honkai3_manage import honkai3_manage

def create(message):
	text=message.get("text")
	pic_hash=message.get("pic_hash")
	pic_guid=message.get("pic_guid")
	audio=message.get("audio")
	message_type=message.get("message_type")
	req_group=message.get("req_group")
	req_id=message.get("req_id")
	# 初始化发送的消息内容
	res_msg={
		"message_type":message.get("message_type"),
		"fromqq":message.get("self_id"),
		"toqq":message.get("req_id"),
		"togroup":message.get("req_group"),
		"anonymous":False,
		"have_text":False,
		"text":"",
		"have_pic":False,
		"pic_type":0,
		"pic_line":"",
		"pic_path":"",
		"pic_url":"",
		"have_audio":False,
		"audio_type":0,
		"audio_line":"",
		"audio_path":"",
		"audio_url":""
	}
	message_check=text.split()

	# 获得消息鉴权
	admin_authority=get_authority("",req_id)
	authority=get_authority(req_group,req_id)

	# 避免自我回复
	if req_id==message.get("self_id"):
		return res_msg

	# 判断权限后获得回复内容
	if (len(message_check)>1 and admin_authority.get("admin") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		if (message_check[0].upper()=="ADMIN" or message_check[0]=="管理员"):
			res_msg["text"]=admin(text)
			if res_msg["text"]!="":
				res_msg["have_text"]=True

	if (len(message_check)>0 and admin_authority.get("honkai3_manage") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		res_msg["text"]=honkai3_manage(text)
		if res_msg["text"]!="":
			res_msg["have_text"]=True

	if (len(message_check)>1 and authority.get("warframe") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		#res_msg["text"]=warframe(text)
		#if res_msg["text"]!="":
			#res_msg["have_text"]=True
		msg_trans=warframe(text)
		if msg_trans!="":
			res_msg["pic_path"]=w2p(msg_trans)
			res_msg["have_pic"]=True
			res_msg["pic_type"]=1
			
	if (len(message_check)>0 and authority.get("honkai3") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		#res_msg["text"]=honkai3(text)
		#if res_msg["text"]!="":
			#res_msg["have_text"]=True
		msg_trans=honkai3(text)
		if msg_trans!="":
			res_msg["pic_path"]=w2p(msg_trans)
			res_msg["have_pic"]=True
			res_msg["pic_type"]=1

	if (len(message_check)>1 and authority.get("nlp_chat") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		res_msg["text"]=tencent(text)
		if res_msg["text"]!="":
			res_msg["have_text"]=True

	if (len(message_check)>1 and authority.get("webcrawler") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		(res_text,msg_type)=crawler(text)
		if res_text!="":
			if msg_type=="pic_url":
				res_msg["pic_url"]=res_text
				res_msg["have_pic"]=True
				res_msg["pic_type"]=2
			elif msg_type=="text":
				res_msg["text"]=res_text
				res_msg["have_text"]=True

	if (len(message_check)>0 and authority.get("game") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		#res_msg["text"]=game(message)
		#if res_msg["text"]!="":
			#res_msg["have_text"]=True
		msg_trans=game(message)
		if msg_trans!="":
			res_msg["pic_path"]=w2p(msg_trans)
			res_msg["have_pic"]=True
			res_msg["pic_type"]=1

	return res_msg
	