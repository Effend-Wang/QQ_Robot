# 该代码用于加载warframe相关数据并存储为全局变量

import os
import database_operate

warframe_db_path=os.getcwd()+"/data/warframe/"

# 加载数据库数据
def warframe_db_loading():

	#global warframe_info_dict
	global warframe_darvo_dict
	global warframe_events_dict
	global warframe_invasions_dict
	global warframe_landscape_dict
	global warframe_market_dict
	global warframe_missiontype_dict
	global warframe_news_dict
	global warframe_nightwave_dict
	global warframe_node_dict
	global warframe_openplain_dict
	global warframe_sortie_dict
	global warframe_translation_dict
	global warframe_voidtrader_dict

	warframe_darvo_dict=var_write(warframe_db_path+"darvo.mdb")
	warframe_events_dict=var_write(warframe_db_path+"events.mdb")
	warframe_invasions_dict=var_write(warframe_db_path+"invasions.mdb")
	warframe_landscape_dict=var_write(warframe_db_path+"landscape.mdb")
	warframe_market_dict=var_write(warframe_db_path+"market.mdb")
	warframe_missiontype_dict=var_write(warframe_db_path+"missiontype.mdb")
	warframe_news_dict=var_write(warframe_db_path+"news.mdb")
	warframe_nightwave_dict=var_write(warframe_db_path+"nightwave.mdb")
	warframe_node_dict=var_write(warframe_db_path+"node.mdb")
	warframe_openplain_dict=var_write(warframe_db_path+"openplain.mdb")
	warframe_sortie_dict=var_write(warframe_db_path+"sortie.mdb")
	warframe_translation_dict=var_write(warframe_db_path+"translation.mdb")
	warframe_voidtrader_dict=var_write(warframe_db_path+"voidtrader.mdb")

# 读取warframe数据库并处理为dict格式数据
def var_write(file_path):
	data=[]
	output_dict={}
	data=database_operate.access_operate("all",None,file_path)
	if data==[]:
		print("文件%s的数据读取出现错误！" %file_path)
	else:
		length=len(data)
		for i in range(length):
			dict_add={data[i][0]:data[i][1]}
			output_dict.update(dict_add)

	return output_dict

# 调用词典
def get_warframe_dict(value):

	if value=="warframe_darvo":
		return warframe_darvo_dict
	elif value=="warframe_events":
		return warframe_events_dict
	elif value=="warframe_invasions":
		return warframe_invasions_dict
	elif value=="warframe_landscape":
		return warframe_landscape_dict
	elif value=="warframe_market":
		return warframe_market_dict
	elif value=="warframe_missiontype":
		return warframe_missiontype_dict
	elif value=="warframe_news":
		return warframe_news_dict
	elif value=="warframe_nightwave":
		return warframe_nightwave_dict
	elif value=="warframe_node":
		return warframe_node_dict
	elif value=="warframe_openplain":
		return warframe_openplain_dict
	elif value=="warframe_sortie":
		return warframe_sortie_dict
	elif value=="warframe_translation":
		return warframe_translation_dict
	elif value=="warframe_voidtrader":
		return warframe_voidtrader_dict