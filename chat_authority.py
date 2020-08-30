# 该文档代码用于控制聊天权限
# 其中get_list()保存权限信息，包括：
#	"id":<string>群号或个人号；
#	"type":<string>号码类型（"group"群号码，"private"个人号码）；
#	"admin":<bool>是否有管理员权限；
#	"warframe":<bool>是否有Warframe模块聊天权限；
#	"honkai3":<bool>是否有崩坏三模块聊天权限；

import database_operate
import os

from config_globalvar import get_config_dict

def get_list(group_id,user_id):
	recent_path=os.getcwd()
	operate="query"
	db_path=recent_path+"/data/config/authority.mdb"
	if group_id=="":
		value="id='"+str(user_id)+"' and type='private'"
	else:
		value="id='"+str(group_id)+"' and type='group'"

	result=database_operate.access_operate(operate,value,db_path)
	#print(result)

	if result==[]:
		chat_list={}
	else:
		chat_list={
			"group_id":group_id,
			"user_id":user_id,
			"type":result[0][1],
			"admin":result[0][2],
			"warframe":result[0][3],
			"honkai3":result[0][4]
		}
	#print(chat_list)

	return chat_list

def get_authority(group_id,user_id):

	authority=False
	chat_list=get_list(group_id,user_id)
	list_length=len(chat_list)
	group_id=str(group_id)
	user_id=str(user_id)
	if (group_id!="" and user_id!="" and chat_list!={}):
		if (str(chat_list.get("group_id"))==group_id and chat_list.get("type")=="group"):
			authority={
				"admin":chat_list.get("admin"),
				"warframe":chat_list.get("warframe"),
				"honkai3":chat_list.get("honkai3")
			}
			#print(authority)
	elif (group_id=="" and user_id!="" and chat_list!={}):
		if (str(chat_list.get("user_id"))==user_id and chat_list.get("type")=="private"):
			authority={
				"admin":chat_list.get("admin"),
				"warframe":chat_list.get("warframe"),
				"honkai3":chat_list.get("honkai3")
			}
			#print(authority)

	return authority
