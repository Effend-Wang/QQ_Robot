# 该文档用于翻译功能
import os
import database_operate

# 数据库结构为 [en, zh]
def game_trans(message_from_user):
	value=message_from_user[2]
	recent_path=os.getcwd()
	operate="query"
	db_path=recent_path+"/data/warframe/warframe_info.mdb"
	if (message_from_user[1]=="zh" or message_from_user[1]=="中文"):
		value="upper(zh)='"+upper(value)+"'"
		result=database_operate.access_operate(operate,value,db_path)
		if result!="":
			after_trans=result[0][0]
	elif (message_from_user[1]=="en" or message_from_user[1]=="英文"):
		value="upper(en)='"+upper(value)+"'"
		result=database_operate.access_operate(operate,value,db_path)
		if result!="":
			after_trans=result[0][0]
	else:
		message_to_send=""

	if result=="":
		message_to_send="\n未能找到翻译内容"
	else:
		message_to_send="\n------翻译："+message_from_user[2]+"------\n"+after_trans

	return message_to_send

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

def market_trans(value):
	after_trans=value
	recent_path=os.getcwd()
	operate="query"
	db_path=recent_path+"/data/warframe/warframe_market.mdb"
	value="upper(zh)='"+upper(value)+"'"
	result=database_operate.access_operate(operate,value,db_path)
	if result!="":
		after_trans=result[0][1]

	return after_trans