# 该代码用于加载tencentcloud相关数据并存储为全局变量

import os
import database_operate

tencent_db_path=os.getcwd()+"/data/tencentcloud/"
tbp_signature_path=tencent_db_path+"/tbpchat/tbp_signature.mdb"
nlp_signatrue_path=tencent_db_path+"/nlpchat/nlp_signature.mdb"

# 加载数据库数据并设置为文件内全局变量
def tencent_db_loading():
	load_check=False

	global tbp_signature
	global nlp_signatrue

	tbp_signature=var_write(tbp_signature_path)
	nlp_signatrue=var_write(nlp_signatrue_path)

# 读取数据库文件
def var_write(file_path):
	data=[]
	output_dict={}
	data=database_operate.access_operate("all",None,file_path)
	if data==[]:
		print("文件%s数据读取出现错误！" %file_path)

	return data

# 调用数据
def get_tencent_list(value):

	if value=="tbp_signature":
		return tbp_signature
	elif value=="nlp_signature":
		return nlp_signatrue
	else:
		return ""