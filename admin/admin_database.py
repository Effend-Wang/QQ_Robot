# 该文档用于admin管理员对数据库的操作
# 程序config相关数据库不可进行操作，以避免可能的程序问题

import os
from database_operate import access_operate

# Warframe数据库
db_warframe={
	"warframe_events":"/data/warframe/warframe_events.mdb",
	"warframe_invasions":"/data/warframe/warframe_invasions.mdb",
	"warframe_landscape":"/data/warframe/warframe_landscape.mdb",
	"warframe_market":"/data/warframe/warframe_market.mdb",
	"warframe_missiontype":"/data/warframe/warframe_missiontype.mdb",
	"warframe_news":"/data/warframe/warframe_news.mdb",
	"warframe_nightwave":"/data/warframe/warframe_nightwave.mdb",
	"warframe_node":"/data/warframe/warframe_node.mdb",
	"warframe_openplain":"/data/warframe/warframe_openplain.mdb",
	"warframe_sortie":"/data/warframe/warframe_sortie.mdb",
	"warframe_translation":"/data/warframe/warframe_translation.mdb",
	"warframe_voidtrader":"/data/warframe/warframe_voidtrader.mdb"
}

def database_owned():
	warframe_db_list="\nWarframe数据库："
	for key,value in db_warframe.items():
		warframe_db_list=warframe_db_list+"\n"+key
	message_to_send="\n可操作数据库列表："+warframe_db_list

	return message_to_send

# 获取数据库地址
def get_path(db_name):
	#recent_path=os.getcwd()
	#print(recent_path)
	#print(db_name)
	#print(db_name.upper())
	#if (db_name.upper()=="WARFRAME_INFO"):
		#db_path=recent_path+db_warframe.get("warframe_info")
	#elif (db_name.upper()=="WARFRAME_MARKET"):
		#db_path=recent_path+warframe_market
	#elif (db_name.upper()=="WARFRAME_GAME"):
		#db_path=recent_path+warframe_game
	#else:
		#return ""

	db_path=os.getcwd()+db_warframe.get(db_name.lower())

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
