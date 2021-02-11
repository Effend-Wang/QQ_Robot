'''

该文档用于admin管理员相关功能的选择
数据库操作接受的数据必须至少包括4个参数

数据库查询命令：
admin query/查询 <database> <字段>=''

数据库添加命令：
admin add/添加 <database> '' '' '' ...

数据库删除命令：
admin delete/删除 <database> <字段>=''

数据库更改命令：
admin update/更改 <database> <字段>='' <字段>=''

'''

# 导入程序模块
import admin.admin_database as admin_database
from warframe.warframe_globalvar import warframe_db_loading
from honkai3.honkai3_globalvar import honkai3_db_loading

# admin管理员功能引入模块
def admin(message_from_user):
	message_to_send=""
	message_check=message_from_user.split()
	if (message_check[1].upper()=="QUERY" or message_check[1]=="查询"):
		message_to_send=admin_database.admin_query(message_from_user)

	elif (message_check[1].upper()=="ADD" or message_check[1]=="添加"):
		message_to_send=admin_database.admin_add(message_from_user)

	elif (message_check[1].upper()=="DELETE" or message_check[1]=="删除"):
		message_to_send=admin_database.admin_delete(message_from_user)
		message_to_send=""

	elif (message_check[1].upper()=="UPDATE" or message_check[1]=="更改"):
		message_to_send=admin_database.admin_update(message_from_user)
		message_to_send=""

	elif (message_check[1]=="数据库"):
		message_to_send=admin_database.database_owned()

	elif (message_check[1].upper()=="DBRELOAD" or message_check[1]=="重载数据库"):
		warframe_db_loading()
		honkai3_db_loading()
		message_to_send="数据库已重载"

	else:
		message_to_send=""

	return message_to_send
