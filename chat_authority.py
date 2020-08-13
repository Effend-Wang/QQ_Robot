# 该文档代码用于控制聊天权限
# 其中get_list()保存权限信息，包括：
#	"id":<string>群号或个人号；
#	"type":<string>号码类型（"group"群号码，"private"个人号码）；
#	"admin":<bool>是否有管理员权限；
#	"warframe":<bool>是否有Warframe模块聊天权限；
#	"honkai3":<bool>是否有崩坏三模块聊天权限；

def get_list():

	chat_list=[
		{
			"id":<string>,
			"type":<string>,
			"admin":<bool>,
			"warframe":<bool>,
			"honkai3":<bool>
		}
	]

	return chat_list

def get_authority(group_id,user_id):

	authority=False
	chat_list=get_list()
	list_length=len(chat_list)
	group_id=str(group_id)
	user_id=str(user_id)
	if (group_id!="" and user_id!=""):
		for i in range(list_length):
			if (chat_list[i].get("id")==group_id and chat_list[i].get("type")=="group"):
				authority={
					"admin":chat_list[i].get("admin"),
					"warframe":chat_list[i].get("warframe"),
					"honkai3":chat_list[i].get("honkai3")
				}
				#print(authority)
				break
	elif (group_id=="" and user_id!=""):
		for i in range(list_length):
			if (chat_list[i].get("id")==user_id and chat_list[i].get("type")=="private"):
				authority={
					"admin":chat_list[i].get("admin"),
					"warframe":chat_list[i].get("warframe"),
					"honkai3":chat_list[i].get("honkai3")
				}
				#print(authority)
				break

	return authority
