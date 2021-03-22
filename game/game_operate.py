'''

该模块用于引入游戏功能，包括：
1、抽一位群友
2、PDG游戏（Pet Develop Game）

'''

# 导入程序模块
from game.pick_friend import pickf
from game.pdg.pdg_operate import pdg
from game.dice import pickd

# 游戏功能引入模块
def game(message):

	message_to_send=""
	msglen=len(message["text"])

	if(message["message_type"]=="group" and (message["text"][0:5]=="抽一位群友" or message["text"][0:3]=="抽群友")):
		message_to_send=pickf(message)

	if(message["text"]=="骰子" or message["text"]=="掷骰子"):
		message_to_send=pickd()

	if(msglen>0):
		message_to_send=pdg(message)

	return message_to_send
