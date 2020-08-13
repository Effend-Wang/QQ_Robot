# 该文档用于进行文字翻译

import warframe.zh as zh
from json import loads

# 翻译到中文（输入的data为array或字符串类型）
def trans_zh(data):
	zh_data=zh.dict()
	if isinstance(data,str):
		after_trans=zh_data.get("Text").get(data)
		if after_trans==None:
			after_trans=zh_data.get("Category").get(data)
		if after_trans==None:
			after_trans=data
	elif isinstance(data,list):
		data_length=len(data)
		after_trans=[]
		for i in range(data_length):
			trans=zh_data.get("Text").get(data[i])
			if trans==None:
				trans=zh_data.get("Category").get(data[i])
			if trans==None:
				trans=data[i]
			after_trans.append(trans)
	else:
		after_trans=data

	return after_trans