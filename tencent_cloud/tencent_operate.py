# 该文档用于接入腾讯云方面功能，并引导至对应模块处理数据

import os
import tencent_cloud.tbp_chat as tbp_chat
import tencent_cloud.nlp_chat as nlp_chat

def tencent(message_from_user):
	message_to_send=""
	message_check=message_from_user.split(" ",1)

	# TBP聊天模块更适合应答聊天，不适合智能聊天，故不再使用
	#if (message_check[0]=="聊天1" or message_check[0].upper()=="CHAT"):
		#message_to_send=tbp_chat.get_tbpchat(message_from_user)
	
	# 智能聊天模块暂时仅采用NLP聊天
	if (message_check[0]=="聊天" or message_check[0].upper()=="CHAT"):
		message_to_send=nlp_chat.get_nlpchat(message_from_user)

	return message_to_send