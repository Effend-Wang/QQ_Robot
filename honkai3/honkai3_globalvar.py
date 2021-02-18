'''

该模块用于加载honkai3相关数据并存储为全局变量

'''

import os
import database_operate

honkai3_db_path=os.getcwd()+"/data/honkai3/"

# 加载数据库数据
def honkai3_db_loading():

	# 全局变量
	#global honkai3_shenyuan_list
	global honkai3_zhanchang_list

	#honkai3_shenyuan_list=var_write(honkai3_db_path+"shenyuan.mdb")
	honkai3_zhanchang_list=var_write(honkai3_db_path+"zhanchang.mdb")

def honkai3_local_loading():
	#global honkai3_recent_shenyuan
	global honkai3_recent_zhanchang

	#honkai3_recent_shenyuan=[]
	honkai3_recent_zhanchang=[]

# 读取honkai3数据库并处理为list格式数据
def var_write(file_path):
	data=[]
	data=database_operate.access_operate("all",None,file_path)
	if data==[]:
		print("文件%s的数据读取出现错误！" %file_path)

	return data

# 调用数据
def get_honkai3_list(value):
	#if value=="honkai3_shenyuan":
		#return honkai3_shenyuan_list
	if value=="honkai3_zhanchang":
		return honkai3_zhanchang_list
	#elif value=="honkai3_recent_shenyuan":
		#return honkai3_recent_shenyuan
	elif value=="honkai3_recent_zhanchang":
		return honkai3_recent_zhanchang

# 修改数据
def recent_change(item,value):
	#global honkai3_recent_shenyuan
	global honkai3_recent_zhanchang

	#if item=="shenyuan":
		#honkai3_recent_shenyuan=value.split()
	if item=="zhanchang":
		honkai3_recent_zhanchang=value.split()
