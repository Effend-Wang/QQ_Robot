'''

该模块用于查询honkai3相关信息，包括：
1、阵容查询；
2、当期战场查询；
3、当期深渊查询；（暂不使用）

'''

# 导入程序模块
from honkai3.honkai3_globalvar import get_honkai3_list

# 查询信息主程序
def get_info(message_from_user):
	message_check=message_from_user.split()
	message_to_send=""
	if message_check[0]=="阵容":
		message_to_send=group(message_check[1])
	#elif message_check[0]=="当期深渊":
		#message_to_send=shenyuan()
	elif message_check[0]=="当期战场":
		message_to_send=zhanchang()

	return message_to_send

# 查询某怪物对应阵容
def group(monster):
	#shenyuan_list=get_honkai3_list("honkai3_shenyuan")
	zhanchang_list=get_honkai3_list("honkai3_zhanchang")
	#sylen=len(shenyuan_list)
	zclen=len(zhanchang_list)
	mlist=[]
	message_to_send=""

	for i in range(zclen):
		if monster==zhanchang_list[i][0]:
			mlist=zhanchang_list[i]
			break

	#for i in range(sylen):
		#if monster==shenyuan_list[i][0]:
			#mlist=shenyuan_list[i]
			#break

	if mlist==[]:
		message_to_send="未查到相关阵容数据！"
		return message_to_send

	message_to_send=message_to_send+"查询【%s】阵容：" %(mlist[0])
	mlist=mlist[1:]
	mlen=len(mlist)
	for i in range(mlen):
		if (mlist[i]==None or mlist[i]==""):
			continue
		else:
			message_to_send=message_to_send+"\n%s、%s" %(i+1,mlist[i])

	return message_to_send

# 查询当期深渊信息（暂不使用）
def shenyuan():
	message_to_send=""
	shenyuan_list=get_honkai3_list("honkai3_shenyuan")
	recent_list=get_honkai3_list("honkai3_recent_shenyuan")
	sylen=len(shenyuan_list)
	relen=len(recent_list)
	result=[]
	if recent_list==[]:
		message_to_send="数据不足，请检查当期深渊列表"
		return message_to_send
	for m in range(relen):
		for n in range(sylen):
			if recent_list[m]==shenyuan_list[n][0]:
				result.append(shenyuan_list[n])
	result_len=len(result)
	if result_len<relen:
		message_to_send="数据不足，请检查当期深渊列表"
		return message_to_send

	message_to_send="当期深渊："
	for m in range(result_len):
		if m!=0:
			message_to_send=message_to_send+"\n【%s】阵容：" %(result[m][0])
		for n in range(len(result[m])-1):
			message_to_send=message_to_send+"\n%s、%s" %(n+1,result[m][n+1])

	return message_to_send

# 查询当期战场信息
def zhanchang():
	message_to_send=""
	zhanchang_list=get_honkai3_list("honkai3_zhanchang")
	recent_list=get_honkai3_list("honkai3_recent_zhanchang")
	zclen=len(zhanchang_list)
	relen=len(recent_list)
	result=[]
	if recent_list==[]:
		message_to_send="数据不足，请检查当期战场列表"
		return message_to_send
	for m in range(relen):
		for n in range(zclen):
			if recent_list[m]==zhanchang_list[n][0]:
				result.append(zhanchang_list[n])
	result_len=len(result)
	if result_len<relen:
		message_to_send="数据不足，请检查当期战场列表"
		return message_to_send

	message_to_send="当期战场："
	for m in range(result_len):
		message_to_send=message_to_send+"\n【%s】阵容：" %(result[m][0])
		for n in range(len(result[m])-1):
			if result[m][n+1]==None or result[m][n+1]=="":
				continue
			else:
				message_to_send=message_to_send+"\n%s、%s" %(n+1,result[m][n+1])
				
	return message_to_send