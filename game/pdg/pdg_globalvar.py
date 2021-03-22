'''

该模块用于加载pdg相关数据并存储为全局变量

'''

import os
import database_operate

pdg_db_path=os.getcwd()+"/data/pdg/global/"

# 加载数据库数据
def pdg_db_loading():

	# 全局变量
	global pdg_character_list
	global pdg_item_list
	global pdg_jewelry_list
	global pdg_level_list
	global pdg_monster_list
	global pdg_skill_list
	global pdg_stage_list
	global pdg_weapon_list

	# 读取数据
	pdg_character_list=var_write(pdg_db_path+"character.mdb")
	pdg_item_list=var_write(pdg_db_path+"item.mdb")
	pdg_jewelry_list=var_write(pdg_db_path+"jewelry.mdb")
	pdg_level_list=var_write(pdg_db_path+"level.mdb")
	pdg_monster_list=var_write(pdg_db_path+"monster.mdb")
	pdg_skill_list=var_write(pdg_db_path+"skill.mdb")
	pdg_stage_list=var_write(pdg_db_path+"stage.mdb")
	pdg_weapon_list=var_write(pdg_db_path+"weapon.mdb")

# 读取pdg数据库并处理为list格式数据
def var_write(file_path):
	data=[]
	data=database_operate.access_operate("all",None,file_path)
	if data==[]:
		print("文件%s的数据读取出现错误！" %file_path)

	return data

# 调用数据
def get_pdg_list(value):
	if value=="pdg_character":
		return pdg_character_list
	elif value=="pdg_item":
		return pdg_item_list
	elif value=="pdg_jewelry":
		return pdg_jewelry_list
	elif value=="pdg_level":
		return pdg_level_list
	elif value=="pdg_monster":
		return pdg_monster_list
	elif value=="pdg_skill":
		return pdg_skill_list
	elif value=="pdg_stage":
		return pdg_stage_list
	elif value=="pdg_weapon":
		return pdg_weapon_list
	else:
		print("无该类型数据：%s" %value)