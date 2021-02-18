'''

该模块代码用于获取聊天权限

模块需要输入需要提取的group_id和user_id
其中当请求为私密信息时，group_id=""

提取的数据为：id,type,admin,warframe,honkai3,nlp_chat,webscrawler,game,honkai3_manage

'''

import database_operate
import os

from config_globalvar import get_config_dict

def get_authority(group_id,user_id):
	authority={
		"admin":False,
		"warframe":False,
		"honkai3":False,
		"nlp_chat":False,
		"webcrawler":False,
		"game":False,
		"honkai3_manage":False
	}
	authlist=get_config_dict("authority")
	list_length=len(authlist)
	group_id=str(group_id)
	user_id=str(user_id)
	
	if group_id=="":
		req_type="private"
		req_id=user_id
	else:
		req_type="group"
		req_id=group_id

	for i in range(list_length):
		if (authlist[i][0]==req_id and authlist[i][1]==req_type):
			authority={
				"admin":authlist[i][2],
				"warframe":authlist[i][3],
				"honkai3":authlist[i][4],
				"nlp_chat":authlist[i][5],
				"webcrawler":authlist[i][6],
				"game":authlist[i][7],
				"honkai3_manage":authlist[i][8]
			}

	return authority
