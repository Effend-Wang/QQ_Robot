# 该文档用于翻译功能
import os
import database_operate

# 数据库结构为 [en, zh]，查询采用模糊查询
def game_trans(message_from_user):
	message_from_user=message_from_user.split(" ",2)
	value=message_from_user[2]
	recent_path=os.getcwd()
	operate="query"
	db_path=recent_path+"/data/warframe/warframe_info.mdb"
	result=[]
	print(message_from_user)
	if (message_from_user[1]=="zh" or message_from_user[1]=="中文"):
		print("查询中文")
		value="zh LIKE '%"+value+"%'"
		result=database_operate.access_operate(operate,value,db_path)
		if result!=[]:
			after_trans=result[0][0]
	elif (message_from_user[1]=="en" or message_from_user[1]=="英文"):
		print("查询英文")
		value="en LIKE '%"+value+"%'"
		result=database_operate.access_operate(operate,value,db_path)
		if result!=[]:
			after_trans=result[0][1]
	else:
		message_to_send=""

	if result==[]:
		message_to_send="\n未能找到翻译内容"
	else:
		message_to_send="\n------翻译："+message_from_user[2]+"------\n"+after_trans

	return message_to_send

# 数据结构为 [en, zh]
def info_trans(value):
	after_trans=value
	recent_path=os.getcwd()
	operate="query"
	db_path=recent_path+"/data/warframe/warframe_info.mdb"
	value="en='"+value+"'"
	result=database_operate.access_operate(operate,value,db_path)
	if result!=[]:
		after_trans=result[0][1]

	return after_trans

# 数据结构为[zh, en]，其中zh字段均为大写
def market_trans(value):
	after_trans=value
	recent_path=os.getcwd()
	operate="query"
	db_path=recent_path+"/data/warframe/warframe_market.mdb"
	value="zh='"+value.upper()+"'"
	result=database_operate.access_operate(operate,value,db_path)
	if result!="":
		after_trans=result[0][1]

	return after_trans