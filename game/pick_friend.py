'''

该模块用于随机抽一个群友的游戏

模块需传入全部的请求数据
模块返回抽选后的文字消息

模块需要使用框架的取群成员列表功能，要求数据包括：
	logonqq：框架qq
	group：群号
api地址：/getgroupmemberlist

'''

from json import loads
import requests
import random

api_url="http://127.0.0.1:10429/getgroupmemberlist"

# 随机抽取一位群友
def pickf(message):

	req_id=message["req_id"]
	req_group=message["req_group"]

	# 从框架获取群成员列表
	data={
		"logonqq":message["self_id"],
		"group":req_group
	}
	r=loads(requests.post(api_url,data=data).text)
	memlist=r.get("List")
	namelist=[]
	listlength=len(memlist)
	for i in range(listlength):
		if (memlist[i].get("Card")==""):
			namelist.append(memlist[i].get("NickName"))
		else:
			namelist.append(memlist[i].get("Card"))
	pf=random.choice(namelist)

	# 获取请求者的昵称
	for i in range(listlength):
		if (memlist[i].get("UIN")==req_id):
			if (memlist[i].get("Card")==""):
				req_name=memlist[i].get("NickName")
			else:
				req_name=memlist[i].get("Card")

	message_to_send=req_name+" 抽到了 "+pf

	return message_to_send
