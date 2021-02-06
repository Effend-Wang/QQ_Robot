# 该模块用于创建回复数据

# 导入程序库
import chat_authority
from warframe.warframe_operate import warframe
from admin.admin_operate import admin
from tencent_cloud.tencent_operate import tencent
from webcrawler.crawler_operate import crawler
from tools.word2pic import w2p

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
	if (len(message_check)<=1):
		return res_msg

	# 获得消息鉴权
	if (message_type=="private"):
		authority=chat_authority.get_authority(req_group,req_id)
		if (authority==False):
			return res_msg
	elif (message_type=="group"):
		authority=chat_authority.get_authority(req_group,req_id)
		if (authority==False):
			return res_msg
	else:
		return res_msg

	# 判断权限后获得回复内容
	if (authority.get("admin") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		if (message_check[0].upper()=="ADMIN"):
			res_msg["text"]=admin(text)
			if res_msg["text"]!="":
				res_msg["have_text"]=True

	if (authority.get("warframe") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		#res_msg["text"]=warframe(text)
		#if res_msg["text"]!="":
			#res_msg["have_text"]=True
		msg_trans=warframe(text)
		if msg_trans!="":
			res_msg["pic_path"]=w2p(msg_trans)
			res_msg["have_pic"]=True
			res_msg["pic_type"]=1
			
	if (authority.get("honkai3") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		pass

	if (authority.get("nlp_chat") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		res_msg["text"]=tencent(text)
		if res_msg["text"]!="":
			res_msg["have_text"]=True

	if (authority.get("webcrawler") and res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		res_msg["pic_url"]=crawler(text)
		if res_msg["pic_url"]!="":
			res_msg["pic_type"]=2
			res_msg["have_pic"]=True

	return res_msg
	