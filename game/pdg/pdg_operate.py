'''

该模块用于PDG游戏模块的操作选择

'''

import game.pdg.pdg_info as pdg_info
import game.pdg.pdg_ingame as pdg_ingame

def pdg(message):
	message_to_send=""
	req_id=message.get("req_id")
	req_msg=message.get("text")
	message_to_send=pdg_info.get_info(req_id,req_msg)
	if message_to_send=="":
		message_to_send=pdg_ingame.ingame(req_id,req_msg)

	return message_to_send