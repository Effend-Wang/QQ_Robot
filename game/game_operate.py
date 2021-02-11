'''

该模块用于引入游戏功能，包括：
1、抽一位群友

'''

# 导入程序模块
from game.pick_friend import pickf

# 游戏功能引入模块
def game(message):

	message_to_send=""
	msglen=len(message["text"])

	if(message["message_type"]=="group" and msglen>=5 and (message["text"][0:5]=="抽一位群友" or message["text"][0:3]=="抽群友")):
		message_to_send=pickf(message)

	return message_to_send
