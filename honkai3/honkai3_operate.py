'''

该模块用于引入崩坏3游戏相关功能，包括：
1、查询游戏信息；（honkai3_info.py）

'''

# 导入程序模块
import honkai3.honkai3_info as honkai3_info

# honkai3游戏相关功能引入
def honkai3(message_from_user):
	message_check=message_from_user.split()
	message_to_send=""
	message_to_send=honkai3_info.get_info(message_from_user)

	return message_to_send