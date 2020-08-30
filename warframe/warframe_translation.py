# 该文档用于翻译功能
import os
import database_operate
from warframe.warframe_globalvar import get_warframe_dict

#db_game="/data/warframe/warframe_translation.mdb"
#db_info="/data/warframe/warframe_info.mdb"
#db_market="/data/warframe/warframe_market.mdb"

# 数据库结构为{en:zh}
def game_trans(message_from_user):
	message_from_user=message_from_user.split(" ",2)
	before_trans=message_from_user[2]
	#recent_path=os.getcwd()
	#operate="query"
	#db_path=recent_path+db_game
	result=""
	#print(message_from_user)
	if (message_from_user[1]=="zh" or message_from_user[1]=="中文"):
		#print("查询中文")
		#value="zh LIKE '%"+value+"%'"
		#result=database_operate.access_operate(operate,value,db_path)
		#if result!=[]:
			#after_trans=result[0][0]
		en2zh=get_warframe_dict("warframe_translation")
		zh2en={}
		for key,value in en2zh.items():
			zh2en[value]=key
		result=zh2en.get(before_trans)

	elif (message_from_user[1]=="en" or message_from_user[1]=="英文"):
		#print("查询英文")
		#value="en LIKE '%"+value+"%'"
		#result=database_operate.access_operate(operate,value,db_path)
		#if result!=[]:
			#after_trans=result[0][1]
		en2zh=get_warframe_dict("warframe_translation")
		result=en2zh.get(before_trans)

	else:
		message_to_send=""

	if result==None:
		message_to_send="\n未能找到翻译内容"
	else:
		message_to_send="\n------翻译："+message_from_user[2]+"------\n"+result

	return message_to_send

# 数据结构为 [en, zh]
def info_trans(data_name,value):
	#after_trans=value
	#recent_path=os.getcwd()
	#operate="query"
	#db_path=recent_path+db_info
	#value="en='"+value+"'"
	#result=database_operate.access_operate(operate,value,db_path)
	data=get_warframe_dict(data_name)
	result=data.get(value)
	if result==None:
		return value
	else:
		return result

# 数据结构为{zh:en}，其中zh字段均为大写
def market_trans(data_name,value):
	#after_trans=value
	#recent_path=os.getcwd()
	#operate="query"
	#db_path=recent_path+db_market
	#value="zh='"+value.upper()+"'"
	#result=database_operate.access_operate(operate,value,db_path)
	data=get_warframe_dict(data_name)
	result=data.get(value.upper())
	if result==None:
		return value
	else:
		return result