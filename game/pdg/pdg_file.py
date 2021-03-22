'''

该模块用于读写PDG游戏玩家存档

'''

# 导入第三方库
import os

# 初始化参数
path=os.getcwd()+"/data/pdg/player/"

# 将玩家数据写入文件
def write_file(data,req_id):
	filepath=path+str(req_id)+".dat"
	with open(filepath,"w") as file:
		for key in data:
			msg=key+" "+str(data[key])+"\n"
			file.write(msg)

# 从文件中读取玩家数据，并返回数据字典
def read_file(req_id):
	filepath=path+str(req_id)+".dat"
	data={}
	
	# 若文件不存在，则直接返回data={}
	if os.path.exists(filepath)==False:
		return data

	# 读取文件
	with open(filepath,"r") as file:
		lines=file.readlines()
		for i in range(len(lines)):
			msg=lines[i].split(" ",1)
			data[msg[0]]=msg[1].replace("\n","")

	return data
