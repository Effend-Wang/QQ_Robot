# 该文档用于admin管理员对数据库的操作

import os
from database_operate import access_operate

warframe_info="/data/warframe/warframe_info.mdb"
warframe_market="/data/warframe/warframe_market.mdb"
warframe_game="/data/warframe/warframe_game.mdb"

def database_owned():
	db_list=["warframe_info","warframe_market","warframe_game"]
	length=len(db_list)
	message_to_send=""
	for i in range(length):
		message_to_send=message_to_send+"\n"+db_list[i]
	message_to_send="\n可操作数据库列表："+message_to_send

	return message_to_send

# 获取数据库地址
def get_path(db_name):
	recent_path=os.getcwd()
	#print(recent_path)
	#print(db_name)
	#print(db_name.upper())
	if (db_name.upper()=="WARFRAME_INFO"):
		db_path=recent_path+warframe_info
	elif (db_name.upper()=="WARFRAME_MARKET"):
		db_path=recent_path+warframe_market
	elif (db_name.upper()=="WARFRAME_GAME"):
		db_path=recent_path+warframe_game
	else:
		return ""

	if os.path.exists(db_path)==False:
		print("Path False")
		return ""

	return db_path

# 从数据库中查询
def admin_query(message_from_user):
	message_from_user=message_from_user.split(" ",3)

	if message_from_user[2]=="格式":
		message_to_send="\n查询数据格式：\nadmin query <database> <字段>=''"
		return message_to_send

	if len(message_from_user)!=4:
		message_to_send="\n输入格式错误！"
		return message_to_send

	operate="query"

	db_path=get_path(message_from_user[2])
	if db_path=="":
		message_to_send="\n数据库名错误！"
		return message_to_send

	value=message_from_user[3]

	result=access_operate(operate,value,db_path)
	if result==[]:
		message_to_send="\n未找到数据！"
	else:
		result=result[0]
		result=",".join(result)

		message_to_send="\n找到数据：\n"+result

	return message_to_send

# 向数据库添加数据
def admin_add(message_from_user):
	message_from_user=message_from_user.split(" ",3)
	if message_from_user[2]=="格式":
		message_to_send="\n添加数据格式：\nadmin add <database> '' ''"
		return message_to_send

	if len(message_from_user)!=4:
		message_to_send="\n输入格式错误！"
		return message_to_send

	operate="add"

	db_path=get_path(message_from_user[2])
	if db_path=="":
		message_to_send="\n数据库名错误！"
		return message_to_send

	value=message_from_user[3]
	value=value.split("' '")
	#print(value)
	value="', '".join(value)
	value="("+value+")"
	#print(value)

	result=access_operate(operate,value,db_path)
	if result==False:
		message_to_send="\n添加数据时发生错误！"
	else:
		message_to_send="\n成功添加数据！"

	return message_to_send

# 删除数据库中数据
def admin_delete(message_from_user):
	message_from_user=message_from_user.split(" ",3)

	if message_from_user[2]=="格式":
		message_to_send="\n删除数据格式：\nadmin delete <database> <字段>=''"
		return message_to_send

	if len(message_from_user)!=4:
		message_to_send="\n输入格式错误！"
		return message_to_send

	operate="delete"

	db_path=get_path(message_from_user[2])
	if db_path=="":
		message_to_send="\n数据库名错误！"
		return message_to_send

	value=message_from_user[3]

	result=access_operate(operate,value,db_path)
	if result==False:
		message_to_send="\n删除数据时发生错误！"
	else:
		message_to_send="\n成功删除数据！"

	return message_to_send

# 对数据库中数据进行更改
def admin_update(message_from_user):
	message_from_user=message_from_user.split(" ",3)

	if message_from_user[2]=="格式":
		message_to_send="\n更改数据格式：\nadmin update <database> <更改后> <字段>=''"
		return message_to_send

	if len(message_from_user)!=4:
		message_to_send="\n输入格式错误！"
		return message_to_send

	operate="delete"

	db_path=get_path(message_from_user[2])
	if db_path=="":
		message_to_send="\n数据库名错误！"
		return message_to_send

	value=message_from_user[3]

	result=access_operate(operate,value,db_path)
	if result==False:
		message_to_send="\n更改数据时发生错误！"
	else:
		message_to_send="\n成功更改数据！"

	return message_to_send
