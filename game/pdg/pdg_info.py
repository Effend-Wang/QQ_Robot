'''

该模块用于PDG游戏查询相关功能

'''

import os
from game.pdg.pdg_globalvar import get_pdg_list
from game.pdg.pdg_file import read_file
import time

# 游戏信息查询功能接入
def get_info(req_id,req_msg):
	message_check=req_msg.split()
	message_to_send=""

	if message_check[0]=="游戏主页":
		message_to_send=pdg_mainpage()
	elif message_check[0]=="角色信息":
		message_to_send=get_data(req_id)
	elif message_check[0]=="查看背包":
		message_to_send=get_backpack(req_id,req_msg)
	elif message_check[0]=="探索列表":
		message_to_send=get_stage(req_msg)
	elif message_check[0]=="商店":
		message_to_send=get_shop()
	elif message_check[0]=="副本信息":
		message_to_send=get_stage_detail(req_msg)
	
	return message_to_send

# 游戏主页输出
def pdg_mainpage():
	message_to_send="【游戏主页】\n输入下列命令进行游戏：\n1、创建角色\n2、重建角色\n3、角色信息\n4、查看背包\n5、探索列表\n6、商店\n7、装备锻造"
	return message_to_send

# 获取角色信息
def get_data(req_id):
	message_to_send=""
	data_path=os.getcwd()+"/data/pdg/player/"+str(req_id)+".dat"
	if os.path.exists(data_path)==False:
		message_to_send="未找到角色信息，请创建角色后使用。命令：创建角色 昵称"
	else:
		data=read_file(req_id)
		(data,next_move)=fresh_status(data)
		total_ability=int((data["power"]+data["strength"])*0.6+(data["intelligence"]+data["charm"])*0.4)
		message_to_send="【角色信息】\n昵称："+data["nickname"]+"\n本名："+data["character"]+"\n种族："+data["race"]+"\n稀有度："+data["rare"]
		message_to_send=message_to_send+"\n武力值："+data["power"]+"\n体力值："+data["strength"]+"\n智力值："+data["intelligence"]+"\n魅力值："+data["charm"]+"\n综合战力："+total_ability+"\n金币："+data["gold"]
		message_to_send=message_to_send+"\n当前状态："+data["status"]+"\n下一行动还需："+next_move+"\n"+data["info"]

	return message_to_send

# 角色状态刷新，每次进行耗时行动前处理并更新状态用作行动判断，以及查询角色信息时处理用于更新状态
# 角色状态：data["status"]（当"无行动"时下次行动还需为默认值"0时0分0秒"；当还未结束行动时status保留，并计算剩余时间）
def fresh_status(data):
	timestamp=int(data["timestamp"])
	roundtime=int(float(data["roundtime"])*3600)
	timenow=int(time.time())

	if (timenow>=(timestamp+roundtime)):
		data["status"]="无行动"
		data["roundtime"]="0"
		data["timestamp"]=str(timenow)
		next_move="0时0分0秒"
	else:
		rest=timenow-timestamp-roundtime
		h=str(int(rest/3600))
		m=str(int((rest-h*3600)/60))
		s=str(int(rest-h*3600-m*60))
		next_move=h+"时"+m+"分"+s+"秒"

	return data,next_move

# 获取角色背包内容
# 当item不存在或为""时表示不存在物品
# 通过命令：查看背包 页数。查看指定页的背包内容，每页最多8个物品
def get_backpack(req_id,req_msg):
	message_to_send=""
	message_check=req_msg.split(" ",1)
	if len(message_check)>1:
		try:
			page=int(message_check[1])
		except:
			message_to_send="请使用正确的命令：查看背包 页数"
			return message_to_send
	else:
		page=1
	data=read_file(req_id)
	if data=={}:
		message_to_send="您还未创建角色，请创建角色后使用。命令：创建角色 昵称"
		return message_to_send
	item=data.get("item")
	if item==None or item=="":
		message_to_send="您的背包中无任何物品"
	else:
		item=item.split(",")
		item_name=[]
		item_num=[]
		for i in range(len(item)):
			item_name.append(item[i].split("-")[0])
			item_num.append(item[i].split("-")[1])
		max_page=int(len(item_name)/8)+1
		if page>max_page:
			message_to_send="超出背包页数，您的背包最多为%s页" %max_page
			return message_to_send
		else:
			if page==max_page:
				start=(page-1)*8
				end=len(item_name)
			else:
				start=(page-1)*8
				end=page*8
			item_name=item_name[start:end]
			item_num=item_num[start:end]
		message_to_send="【背包】%s/%s 页" %(page,max_page)
		for i in range(len(item_name)):
			message_to_send=message_to_send+"\n"+item_name[i]+"："+item_num[i]
		message_to_send=message_to_send

	return message_to_send

# 通过特殊的格式获得随机整数值，数据格式为min-max，返回随机值的字符串格式
def get_random(data):
	return str(random.randint(int(data.split("-")[0]),int(data.split("-")[1])))

# 获取探索副本列表，按章节选取页面
# 通过命令：探索列表 章节。查看指定章节的探索内容
# stage.mdb格式：id,stage,type,sug_ability,normal_item,rare_item,legend_item,normal_rate,rare_rate,legend_rate,monster,monster_rate,gold,exp,time
def get_stage(req_msg):
	# 初始化数据
	message_to_send=""
	stage_list=get_pdg_list("pdg_stage")

	# 检查用户输入命令
	message_check=req_msg.split(" ",1)
	if len(message_check)>1:
		try:
			chapter=int(message_check[1])
		except:
			message_to_send="请使用正确的命令：探索列表 章节"
			return message_to_send
	else:
		chapter=1

	# 获取需要输出的内容列表
	outputlist=[]
	for i in range(len(stage_list)):
		if str(chapter)==stage_list[i][0].split("-")[0]:
			outputlist.append(stage_list[i])
	if outputlist==[]:
		message_to_send="未找到对应章节，请重新选择章节"
		return message_to_send

	# 输出内容
	message_to_send="【探索列表】第%s章：" %chapter
	for i in range(len(outputlist)):
		message_to_send=message_to_send+"\n"+outputlist[i][0]+"、"+outputlist[i][1]+"("+outputlist[i][2]+")"+"，建议战力："+outputlist[i][3]
	message_to_send=message_to_send+"\n使用：探索 副本号，可探索所选副本（如：探索 1-1）\n使用：副本信息 副本号，可查看副本详细信息（如：副本信息 1-1）"

	return message_to_send

# 获取副本的详细信息
# 通过命令：副本信息 副本号。查看该副本号的详细信息
# stage.mdb格式：id,stage,type,sug_ability,normal_item,rare_item,legend_item,normal_rate,rare_rate,legend_rate,monster,monster_rate,gold,exp,time
def get_stage_detail(req_msg):
	# 初始化数据
	message_to_send=""
	stage_list=get_pdg_list("pdg_stage")

	# 检查用户输入命令
	message_check=req_msg.split(" ",1)
	if len(message_check)==1:
		message_to_send="请使用正确的命令：副本信息 副本号"
	else:
		chapter=message_check[1]

	# 获取该副本号下的数据
	stage=[]
	for i in range(len(stage_list)):
		if chapter==stage_list[i][0]:
			stage=stage_list[i]
			break
	if stage==[]:
		message_to_send="不存在该副本号，请重新输入"
		return message_to_send

	# 输出内容
	message_to_send="【副本信息】\n副本%s：%s(%s)\n建议战力：%s\n普通掉落：%s(%s%%)\n稀有掉落：%s(%s%%)\n传说掉落：%s(%s%%)\n遇敌信息：%s(%s%%)\n金币奖励：%s\n经验奖励：%s\n副本用时：%sh" %(stage[0],stage[1],stage[2],stage[3],stage[4],stage[7],stage[5],stage[8],stage[6],stage[9],stage[10],stage[11],stage[12],stage[13],stage[14])

	return message_to_send

def get_shop():
	return "商店暂未开放"
