# 该模块用于引入爬虫程序

import webcrawler.bingimg as bingimg

def crawler(message_from_user):
	message_check=message_from_user.split(" ",1)[1]
	message_to_send=""

	if (message_check.lower()=="picture" or message_check=="美图"):
		message_to_send=bingimg.get_url()

	return message_to_send