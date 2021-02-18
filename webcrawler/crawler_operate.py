# 该模块用于引入爬虫程序

import webcrawler.bingbg as bingbg
import webcrawler.bingimg as bingimg

def crawler(message_from_user):
	message_check=message_from_user.split()
	message_to_send=""
	msg_type=""

	if (message_from_user=="必应 美图" or message_from_user.lower()=="bing 美图"):
		message_to_send=bingbg.get_url()
		msg_type="pic_url"

	#if (message_check[0]=="搜图"):
		#message_to_send=bingimg.get_url(message_from_user)
		#msg_type="pic_url"

	return message_to_send,msg_type