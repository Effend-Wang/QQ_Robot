# 该文档用于腾讯AI开放平台NLP Chat应用接入和处理
# NLP使用HTTPS协议通信，本代码中使用GET方法请求，需要接口鉴权
# 实际使用的签名密钥通过数据库读取和存储，不于实际代码中显示以保证密钥安全性
# 数据库字段格式：<app_name>,<app_id>,<app_key>
# app_name为应用名称，app_id为接口鉴权ID（需计算获得实际签名sign），app_key为接口鉴权密钥

from json import loads
import time
import requests
import random
import hashlib
from urllib import parse
import string
import database_operate
import tencent_cloud.tencent_globalvar as tencent_globalvar

# 初始化
nlpchat_url="https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"

def get_sign(data,app_key):
	lst=[i[0]+"="+parse.quote_plus(str(i[1])) for i in data.items()]
	params="&".join(sorted(lst))
	sort=params+"&app_key="+app_key
	sign=hashlib.md5(sort.encode("utf-8"))
	sign=sign.hexdigest().upper()

	return sign

# 发送请求获得数据并处理
def get_nlpchat(message_from_user):

	# 处理输入参数
	message_from_user=message_from_user.split(" ",1)

	# 初始化发送数据
	nlp_signature=tencent_globalvar.get_tencent_dict("nlp_signature")
	#app_name=nlp_signature[0][0]
	app_id=int(nlp_signature[0][1])
	app_key=nlp_signature[0][2]
	time_stamp=int(time.time())
	nonce_str=''.join(random.sample(string.ascii_letters+string.digits,16)).lower()
	session="10000"
	data={
		"app_id":app_id,
		"time_stamp":time_stamp,
		"nonce_str":nonce_str,
		"question":message_from_user[1],
		"session":session,
	}
	data["sign"]=get_sign(data,app_key)

	headers={
		"Content-Type":"application/x-www-form-urlencoded",
	}

	#time.sleep(1)
	response=requests.get(nlpchat_url,params=data,headers=headers).text
	response=loads(response)

	if response.get("ret")==0:
		message_to_send=response.get("data").get("answer")
	else:
		message_to_send=""

	return message_to_send