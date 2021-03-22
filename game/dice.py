'''

该模块用于游戏中的掷骰子游戏，从1~6中随机抽取一个数

模块无需传入任何内容
模块返回文字结果

'''

# 导入第三方库
import random

# 掷骰子
def pickd():
	choosen=random.choice(["1","2","3","4","5","6"])
	message_to_send="您抽到的数为：%s" %choosen

	return message_to_send