import requests
from json import loads
import warframe.en_wm as en_wm

# API链接
warframe_market_api="https://api.warframe.market/v1"
warframe_market_web="https://warframe.market"
all_items="/items"

def get_market(message_from_user):
	message_from_user=message_from_user.strip().split(" ",1)
	url_name=en_wm.trans_en(message_from_user[1].upper())
	if (url_name==message_from_user[1].upper()):
		message_to_send="\n未能查到相关物品，请检查输入的物品格式！"
	else:
		orders_url=warframe_market_api+all_items+"/"+url_name+"/orders"
		orders_web=warframe_market_web+all_items+"/"+url_name
		data=requests.get(orders_url).text
		data=loads(data)
		if data=={}:
			message_to_send="\n无法查询到"+message_from_user[2]+"的交易信息！"
		else:
			data=data.get("payload").get("orders")
			online_list=[]
			data_length=len(data)
			for i in range(data_length):
				if (data[i].get("user").get("status")=="ingame" and data[i].get("order_type")=="sell" and data[i].get("platform")=="pc" and data[i].get("region")=="en"):
					online_list.append(data[i])
			online_length=len(online_list)
			for i in range(online_length-1):
				ex_flag=False
				for j in range(online_length-i-1):
					if (online_list[j].get("platinum")>online_list[j+1].get("platinum")):
						online_list[j],online_list[j+1]=online_list[j+1],online_list[j]
						ex_flag=True
				if not ex_flag:
					break

			sell_list=""
			for i in range(online_length):
				if (i<10):
					ingame_name=online_list[i].get("user").get("ingame_name")
					platinum=int(online_list[i].get("platinum"))
					reputation=online_list[i].get("user").get("reputation")
					sell_list=sell_list+"\n"+str(i+1)+"、卖家："+ingame_name+"，售价："+str(platinum)+"，信誉点："+str(reputation)
				else:
					break

			if sell_list=="":
				i=-1

			items_url=warframe_market_api+all_items+"/"+url_name
			data=requests.get(items_url).text
			data=loads(data)
			item_name=""
			if data!={}:
				data=data.get("payload").get("item").get("items_in_set")
				items_length=len(data)
				for n in range(items_length):
					if (data[n].get("url_name")==url_name):
						item_name="（"+data[n].get("en").get("item_name")+"）"
						break
			if i>=10:
				i=9

			message_to_send="\n------WM："+message_from_user[1]+item_name+"------\n游戏在线卖家中最低价的"+str(i+1)+"位："+sell_list+"\nWM链接："+orders_web

	return message_to_send


