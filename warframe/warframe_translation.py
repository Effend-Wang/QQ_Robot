# 该文档用于翻译功能

from warframe.zh import trans_zh
from warframe.en import trans_en

def get_trans(message_from_user):
	message_from_user=message_from_user.strip().split(" ",2)
	if len(message_from_user)!=3:
		return ""
		
	if (message_from_user[1]=="中文" or message_from_user[1]=="zh"):
		after_trans=trans_en(message_from_user[2].upper())
	elif (message_from_user[1]=="英文" or message_from_user[1]=="en"):
		after_trans=trans_zh(message_from_user[2].upper())

	if (after_trans==message_from_user[2].upper()):
		message_to_send="\n未能找到相关翻译内容"
	else:
		message_to_send="\n------翻译："+message_from_user[2]+"------\n"+after_trans

	return message_to_send

