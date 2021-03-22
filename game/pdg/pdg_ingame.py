'''

该模块用于PDG游戏操作功能

'''

# 导入第三方库
import os
import random
import time

# 导入程序模块
from game.pdg.pdg_globalvar import get_pdg_list
from game.pdg.pdg_file import write_file
from game.pdg.pdg_file import read_file
from game.pdg.pdg_info import get_info

# 游戏内操作功能引入
def ingame(req_id,req_msg):
	message_to_send=""

	message_check=req_msg.split()
	if message_check[0]=="创建角色" and len(message_check)>1:
		message_to_send=create_role(req_id,req_msg)
	elif message_check[0]=="重建角色" and len(message_check)>1:
		message_to_send=rebuild_role(req_id,req_msg)

	return message_to_send

# 创建新角色
def create_role(req_id,req_msg):
	data_path=os.getcwd()+"/data/pdg/player/"+str(req_id)+".dat"

	if os.path.exists(data_path)==True:
		message_to_send="角色已存在，无需创建角色。若需重新创建，请用命令：重建角色 昵称"
	else:
		character_list=get_pdg_list("pdg_character")
		rare=random.randint(1,100)
		if rare<80:
			rare="普通"
		elif rare<93:
			rare="稀有"
		else:
			rare="传说"
		choose_list=[]
		for i in range(len(character_list)):
			if character_list[i][1]==rare:
				choose_list.append(character_list[i])
		if character_list==None:
			message_to_send="角色数据获取错误！"
		character=random.choice(choose_list)
		data={
			"nickname":req_msg.split(" ",1)[1],
			"character":character[0],
			"rare":character[1],
			"race":character[2],
			"info":character[3],
			"power":get_random(character[4]),
			"strength":get_random(character[5]),
			"intelligence":get_random(character[6]),
			"charm":get_random(character[7]),
			"gold":"0",
			"status":"无行动",
			"roundtime":"0",
			"timestamp":str(int(time.time()))
		}
		write_file(data,req_id)
		message_to_send="角色创建完毕！\n"+get_info(req_id,"角色信息")

	return message_to_send

# 角色重建
def rebuild_role(req_id,req_msg):
	data_path=os.getcwd()+"/data/pdg/player/"+str(req_id)+".dat"

	if os.path.exists(data_path)==False:
		message_to_send="您还未拥有任何角色，如需创建新角色请使用命令：创建角色 昵称"
	else:
		os.remove(data_path)
		message_to_send=create_role(req_id,req_msg)

	return message_to_send

# 通过特殊的格式获得随机整数值，数据格式为min-max，返回随机值的字符串格式
def get_random(data):
	return str(random.randint(int(data.split("-")[0]),int(data.split("-")[1])))
