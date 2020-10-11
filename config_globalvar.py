# 该文件用于加载程序配置数据库数据，并以程序全局变量存储

import os
import database_operate

config_db_path=os.getcwd()+"/data/config/"

# 定义变量并加载数据库数据
def config_db_loading():
	global user_authority

	user_authority=var_write(config_db_path+"/authority.mdb")

# 读取数据库并处理为dict格式数据
def var_write(file_path):
	data=[]
	data=database_operate.access_operate("all",None,file_path)
	if data==[]:
		print("权限文件的数据读取出现错误！")
		return data
	else:
		return data

# 调用数据
def get_config_dict(value):
	if value=="authority":
		return user_authority