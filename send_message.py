'''

该文档代码完成发送消息的操作

模块需提供response.create的返回值
模块为程序的最后一步，不返回任何值

判断群聊消息或私聊消息：提取res_msg中的message_type值

发送文字消息需要的参数有：
	fromqq：发送回复的机器人qq号
	toqq：回复对象的qq号（仅当回复私聊消息时使用）
	togroup：回复对象的群号（仅当回复群消息时使用）
	text：回复的文字消息内容

发送图片消息需要的参数有：
	fromqq：发送回复的机器人qq号
	toqq：回复对象的qq号（仅当回复私聊消息时使用）
	togroup：回复对象的群号（仅当回复群消息时使用）
	fromtype：回复的图片类型（0、1、2）
	pic：图片的pic信息（仅当fromtype为0时使用）
	path：图片的本地绝对路径（仅当fromtype为1时使用）
	url：图片的网络链接地址（仅当fromtype为2时使用）
若fromtype为1或2时，需要先将图片上传，获取pic信息后，再次通过框架api用fromtype=0的形式发送pic信息才会将图片发送出去

'''

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
		