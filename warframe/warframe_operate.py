# 该文档代码用于warframe相关功能的选择

import warframe.warframe_info as warframe_info
import warframe.warframe_market as warframe_market
import warframe.warframe_translation as warframe_translation

def warframe(message_check,message_from_user):
	if (message_check[0].upper()=="CX" or message_check[0]=="查询"):
		message_to_send=warframe_info.get_info(message_from_user)
	elif (message_check[0].upper()=="WM" or message_check[0]=="市场"):
		message_to_send=warframe_market.get_market(message_from_user)
	elif (message_check[0].upper()=="FY" or message_check[0]=="翻译"):
		message_to_send=warframe_translation.get_trans(message_from_user)
	else:
		message_to_send=""

	return message_to_send