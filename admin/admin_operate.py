# 该文档用于admin管理员相关功能的选择
# 数据库操作接受的数据必须包括4个参数： admin <operate> <database> <value>

import admin.admin_database as admin_database
from warframe.warframe_globalvar import warframe_db_loading

def admin(message_from_user):
	message_to_send=""
	message_check=message_from_user.split(" ",3)
	if (message_check[1].upper()=="QUERY" or message_check[1]=="查询"):
		message_to_send=admin_database.admin_query(message_from_user)

	elif (message_check[1].upper()=="ADD" or message_check[1]=="添加"):
		message_to_send=admin_database.admin_add(message_from_user)

	elif (message_check[1].upper()=="DELETE" or message_check[1]=="删除"):
		#message_to_send=admin_database.admin_delete(message_from_user)
		message_to_send=""

	elif (message_check[1].upper()=="UPDATE" or message_check[1]=="更改"):
		#message_to_send=admin_database.admin_update(message_from_user)
		message_to_send=""

	elif (message_check[1]=="数据库"):
		message_to_send=admin_database.database_owned()

	elif (message_check[1].upper()=="DBRELOAD" or message_check[1]=="重载数据库"):
		warframe_db_loading()
		message_to_send=message_to_send+"\n数据库已重载"

	else:
		message_to_send=""

	return message_to_send

