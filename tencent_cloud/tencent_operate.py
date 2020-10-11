# 该文档用于接入腾讯云方面功能，并引导至对应模块处理数据

import os
import tencent_cloud.tbp_chat as tbp_chat
import tencent_cloud.nlp_chat as nlp_chat

def tencent(message_from_user):
	message_to_send=""
	message_check=message_from_user.split(" ",1)
	if (message_check[0]=="聊天1" or message_check[0].upper()=="CHAT"):
		message_to_send=tbp_chat.get_botchat_result(message_from_user)
	if (message_check[0]=="聊天2" or message_check[0].upper()=="CHAT"):
		message_to_send=nlp_chat.get_nlpchat(message_from_user)

	return message_to_send