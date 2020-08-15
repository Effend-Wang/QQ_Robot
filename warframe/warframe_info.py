# 该文档代码用于查询Warframe信息

import requests
from json import loads
import pytz
import time
import datetime
from warframe.warframe_translation import info_trans
import re

# API链接
# API成功链接时回传{"code":200,"message":"OK"}
warframe_api_connect="https://api.warframestat.us/"
warframe_worldstate_api="https://api.warframestat.us/pc/"
# 设置链接头为en，获取英文信息
headers={
	"Accept-Language":"en"
}
# API后缀
alerts="alerts"	# 警报信息及奖励
arbitration="arbitration"	# 仲裁信息
cetus_cycle="cetusCycle"	# 地球平原希图斯日/夜循环信息
conclave_challenge="conclaveChallenges"	# 每日和每周武形秘仪挑战信息
construction_progress="constructionProgress"	# 入侵敌人舰队建造进度
darvo_daily_deal="dailyDeals"	# Darvo每日特惠信息
earth_cycle="earthCycle"	# 地球日/夜循环信息
events="events"	# 事件和战术警报信息
fissures="fissures"	# 虚空遗物任务信息
flash_sales="flashSales"	# 商店热门销售信息
global_upgrades="globalUpgrades"	# 全服奖励信息
invasions="invasions"	# 入侵信息
kuva="kuva"	# 赤毒任务信息
news="news"	# 游戏新闻
nightwave="nightwave"	# 午夜电波信息
persistent_enemy="persistentEnemies"	# Stalker追随者信息
riven_statistic="rivens/search/"	# 紫卡信息查询（需在链接后添加"<riven_name>"）
sentient_outpost="sentientOutposts"	# 航道星舰S船信息
sanctuary="simaris"	# Simaris圣殿状态信息
sortie="sortie"	# 突击信息
syndicate_mission="syndicateMissions"	# 每日集团任务信息
orb_vallis="vallisCycle"	# 奥布山谷冷/暖循环信息
void_trader="voidTrader"	# 虚空商人信息
arcane_enhancement="arcanes/search/"	# 赋能查询（需在链接后添加"{<arcanes_name>}"）

# 查询信息并返回输出信息
def get_info(message_from_user):
	message_to_send=""
	message_from_user=message_from_user.split()

	# 检查是否可链接到API地址，若无法链接则直接返回空字符串
	connect_status=requests.get(warframe_api_connect).text
	connect_status=loads(connect_status)
	if (connect_status.get("code")==200 and connect_status.get("message")=="OK"):
		pass
	else:
		print("注意：Warframe info API无法连接！")
		return ""

	if (message_from_user[1]=="alerts" or message_from_user[1]=="警报"):
		message_to_send=get_alerts()

	elif (message_from_user[1]=="arbitration" or message_from_user[1]=="仲裁"):
		message_to_send=get_arbitration()

	elif (message_from_user[1]=="cetus" or message_from_user[1]=="夜灵平野" or message_from_user[1]=="希图斯" or message_from_user[1]=="地球平原"):
		message_to_send=get_all_cycle()+"\n"+get_cetus_mission()

	elif (message_from_user[1]=="construction" or message_from_user[1]=="巨人战舰" or message_from_user[1]=="豺狼"):
		message_to_send=get_construction_progress()

	elif (message_from_user[1]=="darvo" or message_from_user[1]=="每日特惠"):
		message_to_send=get_darvo_daily_deal()

	elif (message_from_user[1]=="orb" or message_from_user[1]=="奥布山谷" or message_from_user[1]=="福尔图娜" or message_from_user[1]=="金星平原"):
		message_to_send=get_all_cycle()+"\n"+get_orb_mission()

	elif (message_from_user[1]=="events" or message_from_user[1]=="事件" or message_from_user[1]=="战术警报" or message_from_user[1]=="活动"):
		message_to_send=get_events()

	elif (message_from_user[1]=="fissures" or message_from_user[1]=="遗物" or message_from_user[1]=="裂缝" or message_from_user[1]=="核桃" or message_from_user[1]=="虚空"):
		message_to_send=get_fissures()

	elif (message_from_user[1]=="globalupgrades" or message_from_user[1]=="全服加成"):
		message_to_send=get_global_upgrades()

	elif (message_from_user[1]=="invasions" or message_from_user[1]=="入侵"):
		message_to_send=get_invasions()+"\n"+get_construction_progress()

	elif (message_from_user[1]=="kuva" or message_from_user[1]=="赤毒"):
		message_to_send=get_kuva()

	elif (message_from_user[1]=="news" or message_from_user[1]=="新闻"):
		message_to_send=get_news()

	elif (message_from_user[1]=="nightwave" or message_from_user[1]=="午夜电波" or  message_from_user[1]=="电波"):
		message_to_send=get_nightwave()

	elif (message_from_user[1]=="persistent" or message_from_user=="追随者"):
		message_to_send=get_persistent_enemy()

	elif (message_from_user[1]=="riven" or message_from_user[1]=="紫卡"):
		message_to_send=get_riven_statistic()

	elif (message_from_user[1]=="sentient" or message_from_user[1]=="S船" or message_from_user[1]=="s船"):
		message_to_send=get_sentient_outpost()

	elif (message_from_user[1]=="sanctuary" or message_from_user[1]=="simaris" or message_from_user[1]=="圣殿"):
		message_to_send=get_sanctuary()

	elif (message_from_user[1]=="sortie" or message_from_user[1]=="突击"):
		message_to_send=get_sortie()

	elif (message_from_user[1]=="syndicate" or message_from_user[1]=="集团"):
		message_to_send=get_syndicate_mission()

	elif (message_from_user[1]=="voidtrader" or message_from_user[1]=="奸商" or message_from_user[1]=="虚空商人"):
		message_to_send=get_void_trader()

	return message_to_send

# 获取警报内容（该功能暂时无效）
def get_alerts():
	message_to_send=""

	url=warframe_worldstate_api+alerts
	data=requests.get(url,headers=headers).text
	data=loads(data)
	if (data==[]):
		message_to_send=""
	else:
		mission=data.get("mission")
		eta=data.get("eta")
		rewardTypes=data.get("rewardTypes")

	message_to_send=""

	return message_to_send

# 获取仲裁内容
def get_arbitration():

	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+arbitration
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if (data=={}):
		message_to_send="当前无仲裁信息"
	else:
		# 结束时间
		expiry=data.get("expiry")
		rest_time=get_rest_time(expiry)
		# 节点
		node=data.get("node")
		pick_out=re.findall(r'[(](.*?)[)]',node)
		if pick_out==[]:
			node=info_trans(node)
		else:
			pick_out=info_trans(pick_out[0])
			pick_out="("+pick_out+")"
			pattern=re.compile(r'[(](.*?)[)]')
			node=re.sub(pattern,pick_out,node)
		# 敌人类型
		enemy=data.get("enemy")
		# 任务类型
		mission_type=data.get("type")
		mission_type=info_trans(mission_type)

		message_to_send="\n------仲裁信息------"+"\n敌人："+enemy+"\n节点："+node+"\n任务类型："+mission_type+"\n剩余时间："+rest_time

	return message_to_send

# 获取所有循环状态
def get_all_cycle():
	message_to_send=""
	message_to_send="\n------循环信息------"+get_earth_cycle()+get_cetus_cycle()+get_orb_cycle()

	return message_to_send

# 获取地球循环状态
def get_earth_cycle():
	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+earth_cycle
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到地球循环状态"
	else:
		expiry=data.get("expiry")
		isDay=data.get("isDay")
		if isDay:
			state="白天"
		else:
			state="夜晚"
		rest_time=get_rest_time(expiry)

		message_to_send="\n地球："+state+"，剩余时间："+rest_time

	return message_to_send

# 获取夜灵平野循环状态
def get_cetus_cycle():
	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+cetus_cycle
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到夜灵平野循环状态"
	else:
		expiry=data.get("expiry")
		isDay=data.get("isDay")
		if isDay:
			state="白天"
		else:
			state="夜晚"
		rest_time=get_rest_time(expiry)

		message_to_send="\n夜灵平野："+state+"，剩余时间："+rest_time

	return message_to_send

# 获取福尔图娜循环状态
def get_orb_cycle():
	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+orb_vallis
	data=requests.get(url,headers=headers).text
	data=loads(data)
	if data=={}:
		message_to_send="\n未获取到福尔图娜循环状态"
	else:
		expiry=data.get("expiry")
		isDay=data.get("isDay")
		if isDay:
			state="温暖"
		else:
			state="寒冷"
		rest_time=get_rest_time(expiry)

		message_to_send="\n福尔图娜："+state+"，剩余时间："+rest_time

	return message_to_send

# 获取希图斯赏金内容
def get_cetus_mission():
	
	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+syndicate_mission
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到任务信息"
	else:
		all_mission_length=len(data)
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Ostrons"):
				data=data[i]
				status=True
				break
			else:
				status=False

		if status==False:
			message_to_send="\n目前没有希图斯赏金"
			return message_to_send
		
		# 赏金列表
		jobs=data.get("jobs")
		
		# 结束时间
		expiry=data.get("expiry")
		rest_time=get_rest_time(expiry)

		job_number=5
		for i in range(job_number):
			
			# 赏金奖励
			job_reward=jobs[i].get("rewardPool")
			reward_length=len(job_reward)
			rewards=""
			for n in range(reward_length):
				rewards=rewards+info_trans(job_reward[n])+"；"
			
			# 赏金名
			job_type=jobs[i].get("type")
			job_type=info_trans(job_type)

			message_to_send=message_to_send+"\n------赏金"+str(i+1)+"："+job_type+"------\n奖励："+rewards
		
		message_to_send="\n------希图斯赏金信息------\n赏金剩余时间："+rest_time+message_to_send

	return message_to_send

# 获取Darvo的每日特惠内容：
def get_darvo_daily_deal():
	message_to_send=""
	url=warframe_worldstate_api+darvo_daily_deal
	data=requests.get(url,headers=headers).text
	data=loads(data)
	if data==[]:
		message_to_send="\n未获取到Darvo每日特惠信息"
	else:
		data=data[0]
		item=data.get("item")
		item=info_trans(item)
		expiry=data.get("expiry")
		originalprice=data.get("originalPrice")
		saleprice=data.get("salePrice")
		total=data.get("total")
		sold=data.get("sold")
		rest_number=total-sold
		rest_time=get_rest_time(expiry)
		discount=data.get("discount")

		message_to_send="\n------Darvo的每日特惠------"+"\n物品："+item+"\n原价："+str(originalprice)+"\n售价："+str(saleprice)+"\n折扣："+str(discount)+"%"+"\n剩余量："+str(rest_number)+"\n剩余时间："+rest_time

	return message_to_send

# 获取福尔图娜赏金内容
def get_orb_mission():
	
	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+syndicate_mission
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到任务信息"
	else:
		all_mission_length=len(data)
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Solaris United"):
				data=data[i]
				status=True
				break
			else:
				status=False

		if status==False:
			message_to_send="\n目前没有福尔图娜赏金"
			return message_to_send
		
		# 赏金列表
		jobs=data.get("jobs")
		
		# 结束时间
		expiry=data.get("expiry")
		rest_time=get_rest_time(expiry)

		job_number=5
		for i in range(job_number):
			
			# 赏金奖励
			job_reward=jobs[i].get("rewardPool")
			reward_length=len(job_reward)
			rewards=""
			for n in range(reward_length):
				rewards=rewards+info_trans(job_reward[n])+"；"
			
			# 赏金名
			job_type=jobs[i].get("type")
			job_type=info_trans(job_type)

			message_to_send=message_to_send+"\n------赏金"+str(i+1)+"："+job_type+"------\n奖励："+rewards
		
		message_to_send="\n------福尔图娜赏金信息------\n赏金剩余时间："+rest_time+message_to_send

	return message_to_send

# 获得事件活动内容
def get_events():
	
	# 初始化
	message_to_send=""
	url=warframe_worldstate_api+events
	data=requests.get(url,headers=headers).text
	data=loads(data)
	
	if data==[]:
		message_to_send="\n未获取到事件活动信息"
	else:
		all_events_length=len(data)
		event_message=""
		
		for i in range(all_events_length):

			# 结束时间
			expiry=data[i].get("expiry")
			rest_time=get_rest_time(expiry)

			# 事件描述
			description=data[i].get("description")
			description=info_trans(description)

			maximumscore=data[i].get("maximumScore")
			currentscore=data[i].get("currentScore")

			# 节点
			node=data[i].get("node")
			pick_out=re.findall(r'[(](.*?)[)]', node)
			if pick_out==[]:
				node=info_trans(node)
			else:
				pick_out=info_trans(pick_out[0])
				pick_out="("+pick_out+")"
				pattern=re.compile(r'[(](.*?)[)]')
				node=re.sub(pattern,pick_out,node)

			# 事件阶段奖励
			interimsteps=data[i].get("interimSteps")
			interimsteps_length=len(interimsteps)
			rewards=""
			if (interimsteps_length!=0):
				for n in range(interimsteps_length):
					rewards_list=interimsteps[n].get("reward").get("asString").split(" + ")
					if rewards_list==[""]:
						rewards_message="无奖励"
					else:
						rewards_message=""
						rewards_list=info_trans(rewards_list)
						for m in range(len(rewards_list)):
							rewards_message=rewards_message+rewards_list[m]+"；"
					rewards=rewards+"\n阶段"+str(n+1)+"："+rewards_message
			event_message=event_message+"\n\n事件"+str(i+1)+"："+description+"\n剩余时间："+rest_time+"\n事件节点："+node+"\n奖励内容："+rewards

		message_to_send="\n------事件活动------"+event_message

	return message_to_send

# 获取虚空裂缝任务内容
def get_fissures():
	message_to_send=""

	url=warframe_worldstate_api+fissures
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到虚空裂缝任务信息"
	else:
		all_fissures_length=len(data)
		lith_message="\n\n------T1古纪裂缝------"
		meso_message="\n\n------T2前纪裂缝------"
		neo_message="\n\n------T3中纪裂缝------"
		axi_message="\n\n------T4后纪裂缝------"
		requiem_message="\n\n------T5安魂裂缝------"

		for i in range(all_fissures_length):

			# T1古纪虚空遗物任务
			if (data[i].get("tier")=="Lith"):
				# 结束时间
				expiry=data[i].get("expiry")
				rest_time=get_rest_time(expiry)
				# 节点
				node=data[i].get("node")
				pick_out=re.findall(r'[(](.*?)[)]', node)
				if pick_out==[]:
					node=info_trans(node)
				else:
					pick_out=info_trans(pick_out[0])
					pick_out="("+pick_out+")"
					pattern=re.compile(r'[(](.*?)[)]')
					node=re.sub(pattern,pick_out,node)
				# 任务类型
				missiontype=data[i].get("missionType")
				missiontype=info_trans(missiontype)
				# 敌人类型
				enemy=data[i].get("enemy")

				lith_message=lith_message+"\n\n节点："+node+"\n任务类型："+missiontype+"\n敌人类型："+enemy+"\n剩余时间："+rest_time

			# T2前纪虚空遗物任务
			if (data[i].get("tier")=="Meso"):
				# 结束时间
				expiry=data[i].get("expiry")
				rest_time=get_rest_time(expiry)
				# 节点
				node=data[i].get("node")
				pick_out=re.findall(r'[(](.*?)[)]', node)
				if pick_out==[]:
					node=info_trans(node)
				else:
					pick_out=info_trans(pick_out[0])
					pick_out="("+pick_out+")"
					pattern=re.compile(r'[(](.*?)[)]')
					node=re.sub(pattern,pick_out,node)
				# 任务类型
				missiontype=data[i].get("missionType")
				missiontype=info_trans(missiontype)
				# 敌人类型
				enemy=data[i].get("enemy")
				
				meso_message=meso_message+"\n\n节点："+node+"\n任务类型："+missiontype+"\n敌人类型："+enemy+"\n剩余时间："+rest_time

			# T3中纪虚空遗物任务
			if (data[i].get("tier")=="Neo"):
				# 结束时间
				expiry=data[i].get("expiry")
				rest_time=get_rest_time(expiry)
				# 节点
				node=data[i].get("node")
				pick_out=re.findall(r'[(](.*?)[)]', node)
				if pick_out==[]:
					node=info_trans(node)
				else:
					pick_out=info_trans(pick_out[0])
					pick_out="("+pick_out+")"
					pattern=re.compile(r'[(](.*?)[)]')
					node=re.sub(pattern,pick_out,node)
				# 任务类型
				missiontype=data[i].get("missionType")
				missiontype=info_trans(missiontype)
				# 敌人类型
				enemy=data[i].get("enemy")

				neo_message=neo_message+"\n\n节点："+node+"\n任务类型："+missiontype+"\n敌人类型："+enemy+"\n剩余时间："+rest_time

			# T4后纪虚空遗物任务
			if (data[i].get("tier")=="Axi"):
				# 结束时间
				expiry=data[i].get("expiry")
				rest_time=get_rest_time(expiry)
				# 节点
				node=data[i].get("node")
				pick_out=re.findall(r'[(](.*?)[)]', node)
				if pick_out==[]:
					node=info_trans(node)
				else:
					pick_out=info_trans(pick_out[0])
					pick_out="("+pick_out+")"
					pattern=re.compile(r'[(](.*?)[)]')
					node=re.sub(pattern,pick_out,node)
				# 任务类型
				missiontype=data[i].get("missionType")
				missiontype=info_trans(missiontype)
				# 敌人类型
				enemy=data[i].get("enemy")

				axi_message=axi_message+"\n\n节点："+node+"\n任务类型："+missiontype+"\n敌人类型："+enemy+"\n剩余时间："+rest_time

			# T5安魂虚空遗物任务
			if (data[i].get("tier")=="Requiem"):
				# 结束时间
				expiry=data[i].get("expiry")
				rest_time=get_rest_time(expiry)
				# 节点
				node=data[i].get("node")
				pick_out=re.findall(r'[(](.*?)[)]', node)
				if pick_out==[]:
					node=info_trans(node)
				else:
					pick_out=info_trans(pick_out[0])
					pick_out="("+pick_out+")"
					pattern=re.compile(r'[(](.*?)[)]')
					node=re.sub(pattern,pick_out,node)
				# 任务类型
				missiontype=data[i].get("missionType")
				missiontype=info_trans(missiontype)
				# 敌人类型
				enemy=data[i].get("enemy")

				requiem_message=requiem_message+"\n\n节点："+node+"\n任务类型："+missiontype+"\n敌人类型："+enemy+"\n剩余时间："+rest_time

		message_to_send="\n------虚空裂缝任务------"+lith_message+meso_message+neo_message+axi_message+requiem_message

	return message_to_send

# 获取全服加成信息，暂时未开发
def get_global_upgrades():
	message_to_send=""

	return message_to_send

# 获取入侵任务内容
def get_invasions():
	message_to_send=""
	url=warframe_worldstate_api+invasions
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到入侵任务信息"
	else:
		all_mission_length=len(data)
		mission_list=""
		for i in range(all_mission_length):
			single_mission=""
			if (data[i].get("completed")==False and data[i].get("completion")>=0):
				# 节点
				node=data[i].get("node")
				pick_out=re.findall(r'[(](.*?)[)]',node)
				if pick_out==[]:
					node=info_trans(node)
				else:
					pick_out=info_trans(pick_out[0])
					pick_out="("+pick_out+")"
					pattern=re.compile(r'[(](.*?)[)]')
					node=re.sub(pattern,pick_out,node)
				# 入侵描述
				desc=data[i].get("desc")
				desc=info_trans(desc)
				# 攻击方和奖励
				attacker=data[i].get("attackingFaction")
				attackreward=data[i].get("attackerReward").get("asString")
				attackreward=info_trans(attackreward)
				# 防守方和奖励
				defender=data[i].get("defendingFaction")
				defendreward=data[i].get("defenderReward").get("asString")
				defendreward=info_trans(defendreward)

				# 进度
				process=data[i].get("completion")

				# 剩余战斗次数
				count=data[i].get("count")
				requiredruns=data[i].get("requiredRuns")
				if attacker=="Infested":
					attack_rest=0
				else:
					attack_rest=requiredruns-count
				defend_rest=requiredruns+count

				mission_list=mission_list+"\n------"+node+"："+desc+"------\n攻击方："+attacker+"\n奖励："+attackreward+"\n攻方进度："+str(round(process,2))+"%\n剩余攻击次数："+str(attack_rest)+"\n\n防守方："+defender+"\n奖励："+defendreward+"\n守方进度："+str(round(100-process,2))+"%\n剩余防守次数："+str(defend_rest)

		message_to_send="\n------入侵任务------"+mission_list

	return message_to_send

# 获取巨人舰队和利刃豺狼的建造进度
def get_construction_progress():
	message_to_send=""
	url=warframe_worldstate_api+construction_progress
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到巨人战舰或利刃豺狼信息"
	else:
		fomorian=data.get("fomorianProgress")
		razorback=data.get("razorbackProgress")
		message_to_send="\n------入侵建造情况------\n巨人战舰："+fomorian+"%\n利刃豺狼："+razorback+"%"

	return message_to_send

# 获取赤毒任务
def get_kuva():
	message_to_send=""
	url=warframe_worldstate_api+kuva
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到赤毒虹吸器任务信息\n（注意：该查询模块不稳定，基本查不到内容，无解……）"
	else:
		all_mission_length=len(data)
		mission_list=""
		for i in range(all_mission_length):
			expiry=data[i].get("expiry")
			rest_time=get_rest_time(expiry)
			node=data[i].get("node")
			pick_out=re.findall(r'[(](.*?)[)]',node)
			if pick_out==[]:
				node=info_trans(node)
			else:
				pick_out=info_trans(pick_out[0])
				pick_out="("+pick_out+")"
				pattern=re.compile(r'[(](.*?)[)]')
				node=re.sub(pattern,pick_out,node)
			enemy=data[i].get("enemy")
			mission_type=data[i].get("type")
			mission_list=mission_list+"\n\n-----"+node+"\n------\n任务类型："+mission_type+"\n敌人："+enemy+"\n剩余时间："+rest_time

		message_to_send="\n------赤毒虹吸器任务------"+mission_list

	return message_to_send

# 获取游戏新闻内容
def get_news():
	message_to_send=""
	url=warframe_worldstate_api+news
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data==[]:
		message_to_send="\n未获取到新闻内容"
	else:
		all_news_length=len(data)
		news_list=""
		for i in range(all_news_length):
			link=data[i].get("link")
			message=data[i].get("translations").get("zh")
			if message==None:
				message=data[i].get("translations").get("en")
			news_list=news_list+"\n\n新闻"+str(i+1)+"："+message+"\n新闻链接："+link

		message_to_send="\n------新闻列表------"+news_list

	return message_to_send

# 获取午夜电波任务
def get_nightwave():
	message_to_send=""
	url=warframe_worldstate_api+nightwave
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到午夜电波信息"
	else:
		data=data.get("activeChallenges")
		all_challenges_length=len(data)
		daily=""
		week=""
		for i in range(all_challenges_length):
			title=data[i].get("title")
			title=info_trans(title)
			desc=data[i].get("desc")
			desc=info_trans(desc)
			reputation=data[i].get("reputation")
			# 获取每日任务
			if data[i].get("isDaily"):
				daily=daily+"\n任务："+title+"，要求："+desc+"，声望："+str(reputation)
			else:
				week=week+"\n任务："+title+"，要求："+desc+"，声望："+str(reputation)

		message_to_send="\n------午夜电波任务------\n------每日任务------"+daily+"\n------每周任务------"+week

	return message_to_send

def get_persistent_enemy():
	message_to_send=""

	return message_to_send

def get_riven_statistic():
	message_to_send=""

	return message_to_send

# 获取航道星舰S船出没信息
def get_sentient_outpost():
	message_to_send=""
	url=warframe_worldstate_api+sentient_outpost
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到S船出没信息"
	else:
		node=data.get("mission").get("node")
		pick_out=re.findall(r'[(](.*?)[)]',node)
		if pick_out==[]:
			node=info_trans(node)
		else:
			pick_out=info_trans(pick_out[0])
			pick_out="("+pick_out+")"
			pattern=re.compile(r'[(](.*?)[)]')
			node=re.sub(pattern,"",node).rstrip()
			node=info_trans(node)
			node=node+" "+pick_out

		expiry=data.get("expiry")
		rest_time=get_rest_time(expiry)
		message_to_send="\n------S船出没信息------\n出没节点："+node+"\n剩余时间："+rest_time

	return message_to_send

# 查询Simaris任务信息，由于查询内容无意义，不再开发
def get_sanctuary():
	message_to_send=""
	url=warframe_worldstate_api+sanctuary
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到Simaris任务信息"
	else:
		target=data.get("target")
		message_to_send="\n------Simaris任务------\n任务目标："+target

	message_to_send=""	# 该查询内容毫无意义

	return message_to_send

# 获取突击任务信息
def get_sortie():
	message_to_send=""
	url=warframe_worldstate_api+sortie
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到突击任务信息"
	else:
		boss=data.get("boss")
		mission_list=data.get("variants")
		all_mission_length=len(mission_list)
		sortie_mission=""
		for i in range(all_mission_length):
			mission_type=mission_list[i].get("missionType")
			mission_type=info_trans(mission_type)
			modifier=mission_list[i].get("modifier")
			modifier=info_trans(modifier)
			node=mission_list[i].get("node")
			pick_out=re.findall(r'[(](.*?)[)]',node)
			if pick_out==[]:
				node=info_trans(node)
			else:
				pick_out=info_trans(pick_out[0])
				pick_out="("+pick_out+")"
				pattern=re.compile(r'[(](.*?)[)]')
				node=re.sub(pattern,pick_out,node)
			sortie_mission=sortie_mission+"\n------突击"+str(i+1)+"："+node+"------\n任务："+mission_type+"\n状态："+modifier

		message_to_send="\n------突击任务：击败"+boss+"的部队------"+sortie_mission

	return message_to_send

# 获取集团任务
def get_syndicate_mission():
	message_to_send=""

	url=warframe_worldstate_api+syndicate_mission
	data=requests.get(url,headers=headers).text
	data=loads(data)
	if data==[]:
		message_to_send="\n未获取到任务信息"
	else:
		all_mission_length=len(data)

		# 钢铁防线集团
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Steel Meridian"):
				nodes=data[i].get("nodes")

				nodes_length=len(nodes)
				steel_meridian="\n钢铁防线："
				for n in range(nodes_length):
					single_node=nodes[n]
					pick_out=re.findall(r'[(](.*?)[)]',single_node)
					if pick_out==[]:
						single_node=info_trans(single_node)
					else:
						pick_out=info_trans(pick_out[0])
						pick_out="("+pick_out+")"
						pattern=re.compile(r'[(](.*?)[)]')
						nodes[n]=re.sub(pattern,pick_out,single_node)
					steel_meridian=steel_meridian+nodes[n]+"；"
				break
			else:
				steel_meridian="\n目前没有钢铁防线任务"
		

		# 均衡仲裁者集团
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Arbiters of Hexis"):
				nodes=data[i].get("nodes")
				nodes_length=len(nodes)
				arbiters_of_hexis="\n\n均衡仲裁者："
				for n in range(nodes_length):
					single_node=nodes[n]
					pick_out=re.findall(r'[(](.*?)[)]',single_node)
					if pick_out==[]:
						single_node=info_trans(single_node)
					else:
						pick_out=info_trans(pick_out[0])
						pick_out="("+pick_out+")"
						pattern=re.compile(r'[(](.*?)[)]')
						nodes[n]=re.sub(pattern,pick_out,single_node)
					arbiters_of_hexis=arbiters_of_hexis+nodes[n]+"；"
				break
			else:
				arbiters_of_hexis="\n目前没有均衡仲裁者任务"

		# 中枢苏达集团
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Cephalon Suda"):
				nodes=data[i].get("nodes")
				nodes_length=len(nodes)
				cephalon_suda="\n\n中枢苏达："
				for n in range(nodes_length):
					single_node=nodes[n]
					pick_out=re.findall(r'[(](.*?)[)]',single_node)
					if pick_out==[]:
						single_node=info_trans(single_node)
					else:
						pick_out=info_trans(pick_out[0])
						pick_out="("+pick_out+")"
						pattern=re.compile(r'[(](.*?)[)]')
						nodes[n]=re.sub(pattern,pick_out,single_node)
					cephalon_suda=cephalon_suda+nodes[n]+"；"
				break
			else:
				cephalon_suda="\n目前没有中枢苏达任务"

		# 佩兰数列集团
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Perrin Sequence"):
				nodes=data[i].get("nodes")
				nodes_length=len(nodes)
				perrin_sequence="\n\n佩兰数列："
				for n in range(nodes_length):
					single_node=nodes[n]
					pick_out=re.findall(r'[(](.*?)[)]',single_node)
					if pick_out==[]:
						single_node=info_trans(single_node)
					else:
						pick_out=info_trans(pick_out[0])
						pick_out="("+pick_out+")"
						pattern=re.compile(r'[(](.*?)[)]')
						nodes[n]=re.sub(pattern,pick_out,single_node)
					perrin_sequence=perrin_sequence+nodes[n]+"；"
				break
			else:
				perrin_sequence="\n目前没有佩兰数列任务"

		# 血色面纱集团
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="Red Veil"):
				nodes=data[i].get("nodes")
				nodes_length=len(nodes)
				red_veil="\n\n血色面纱："
				for n in range(nodes_length):
					single_node=nodes[n]
					pick_out=re.findall(r'[(](.*?)[)]',single_node)
					if pick_out==[]:
						single_node=info_trans(single_node)
					else:
						pick_out=info_trans(pick_out[0])
						pick_out="("+pick_out+")"
						pattern=re.compile(r'[(](.*?)[)]')
						nodes[n]=re.sub(pattern,pick_out,single_node)
					red_veil=red_veil+nodes[n]+"；"
				break
			else:
				red_veil="\n目前没有血色面纱任务"

		# 新世间集团
		for i in range(all_mission_length):
			if (data[i].get("syndicate")=="New Loka"):
				nodes=data[i].get("nodes")
				nodes_length=len(nodes)
				new_loka="\n\n新世间："
				for n in range(nodes_length):
					single_node=nodes[n]
					pick_out=re.findall(r'[(](.*?)[)]',single_node)
					if pick_out==[]:
						single_node=info_trans(single_node)
					else:
						pick_out=info_trans(pick_out[0])
						pick_out="("+pick_out+")"
						pattern=re.compile(r'[(](.*?)[)]')
						nodes[n]=re.sub(pattern,pick_out,single_node)
					new_loka=new_loka+nodes[n]+"；"
				break
			else:
				new_loka="\n目前没有新世间任务"

	message_to_send="\n------集团任务信息------"+steel_meridian+arbiters_of_hexis+cephalon_suda+perrin_sequence+red_veil+new_loka

	return message_to_send

# 获取虚空商人内容
def get_void_trader():
	message_to_send=""
	url=warframe_worldstate_api+void_trader
	data=requests.get(url,headers=headers).text
	data=loads(data)

	if data=={}:
		message_to_send="\n未获取到虚空商人信息"
	else:
		
		location=data.get("location")
		pick_out=re.findall(r'[(](.*?)[)]',location)
		if pick_out==[]:
			location=info_trans(location)
		else:
			pick_out=info_trans(pick_out[0])
			pick_out="("+pick_out+")"
			pattern=re.compile(r'[(](.*?)[)]')
			location=re.sub(pattern,"",location).rstrip()
			location=info_trans(location)
			location=location+" "+pick_out
		inventory=data.get("inventory")
		active=data.get("active")
		# 虚空商人已经到来
		if active:
			expiry=data.get("expiry")
			rest_time=get_rest_time(expiry)
			inventory_list=""
			for i in range(len(inventory)):
				item=inventory[i].get("item")
				item=info_trans(item)
				credits=inventory[i].get("credits")
				ducats=inventory[i].get("ducats")
				inventory_list=inventory_list+"\n"+str(i+1)+"、"+item+"，奸商币："+str(ducats)+"，星币："+str(credits)
			trader_message="\n出没节点："+location+"\n离开剩余时间："+rest_time+"\n------携带物品------"+inventory_list
		else:
			activation=data.get("activation")
			rest_time=get_rest_time(activation)
			trader_message="\n虚空商人还未到来！\n下次出没节点："+location+"\n到来剩余时间："+rest_time

		message_to_send="\n------虚空商人------"+trader_message

	return message_to_send

# 计算剩余时间
def get_rest_time(expiry):

	gmt=pytz.timezone("GMT")
	gmt=datetime.datetime.now(gmt).strftime("%Y-%m-%dT%H:%M:%S")
	expiry=datetime.datetime.strptime(expiry,"%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S")
	gmt=datetime.datetime.strptime(gmt,"%Y-%m-%dT%H:%M:%S")
	expiry=datetime.datetime.strptime(expiry,"%Y-%m-%dT%H:%M:%S")
	rest_time=str(expiry-gmt)

	return rest_time