# 该文档代码完成发送消息的操作

# 发送的消息内容
#message={
#	"message_type":message_type,
#	"cq_status":at_status,
#	"cq_id":at_id,
#	"group_id":group_id,
#	"user_id":user_id,
#	"nickname":nickname,
#	"message":message,
#	"image_url":image_url,
#	"message_status":message_status
#}

from json import loads
import os

import requests
import response

api_ip="http://127.0.0.1:10429/"
msg_prv_api="sendprivatemsg"
pic_prv_api="sendprivatepic"
aud_prv_api="sendprivateaudio"
msg_gro_api="sendgroupmsg"
pic_gro_api="sendgrouppic"
aud_gro_api="sendgroupaudio"

# 消息发送模块主程序
def send(res_msg):

	if (res_msg["have_text"]==False and res_msg["have_pic"]==False and res_msg["have_audio"]==False):
		return ""

	# 发送消息
	if (res_msg["message_type"]=="private"):
		if (res_msg["have_text"]==True):
			data={
				"fromqq":res_msg["fromqq"],
				"toqq":res_msg["toqq"],
				"text":res_msg["text"]
			}
			api_url=api_ip+msg_prv_api
		if (res_msg["have_pic"]==True):
			path=os.getcwd()+"/testimg.jpg"
			data={
				"fromqq":res_msg["fromqq"],
				"toqq":res_msg["toqq"],
				"fromtype":res_msg["pic_type"],
			}
			if (data["fromtype"]==0):
				data["pic"]=res_msg["pic_line"]
			elif (data["fromtype"]==1):
				data["path"]=res_msg["pic_path"]
			elif (data["fromtype"]==2):
				data["url"]=res_msg["pic_url"]
			api_url=api_ip+pic_prv_api
			r=loads(requests.post(api_url,data=data).text)
			data={
				"fromqq":res_msg["fromqq"],
				"toqq":res_msg["toqq"],
				"text":r.get("ret"),
			}
			api_url=api_ip+msg_prv_api

		if (res_msg["have_audio"]==True):
			data={
				"fromqq":res_msg["fromqq"],
				"toqq":res_msg["toqq"],
				"fromtype":res_msg["audio_type"],
			}
			if (data["fromtype"]==0):
				data["audio"]=res_msg["audio_line"]
			elif (data["fromtype"]==1):
				data["path"]=res_msg["audio_path"]
			elif (data["fromtype"]==2):
				data["url"]=res_msg["audio_url"]
			api_url=api_ip+aud_prv_api
		r=requests.post(api_url,data=data)

	elif (res_msg["message_type"]=="group"):
		if (res_msg["have_text"]==True):
			data={
				"fromqq":res_msg["fromqq"],
				"togroup":res_msg["togroup"],
				"text":res_msg["text"]
			}
			api_url=api_ip+msg_gro_api
		if (res_msg["have_pic"]==True):
			data={
				"fromqq":res_msg["fromqq"],
				"togroup":res_msg["togroup"],
				"fromtype":res_msg["pic_type"]
			}
			if (data["fromtype"]==0):
				data["pic"]=res_msg["pic_line"]
			elif (data["fromtype"]==1):
				data["path"]=res_msg["pic_path"]
			elif (data["fromtype"]==2):
				data["url"]=res_msg["pic_url"]
			api_url=api_ip+pic_gro_api
			r=loads(requests.post(api_url,data=data).text)
			data={
				"fromqq":res_msg["fromqq"],
				"togroup":res_msg["togroup"],
				"text":r.get("ret"),
			}
			api_url=api_ip+msg_gro_api
		if (res_msg["have_audio"]==True):
			data={
				"fromqq":res_msg["fromqq"],
				"togroup":res_msg["togroup"],
				"fromtype":res_msg["audio_type"]
			}
			if (data["fromtype"]==0):
				data["audio"]=res_msg["audio_line"]
			elif (data["fromtype"]==1):
				data["path"]=res_msg["audio_path"]
			elif (data["fromtype"]==2):
				data["url"]=res_msg["audio_url"]
			api_url=api_ip+aud_gro_api
		r=requests.post(api_url,data=data)
		