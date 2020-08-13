// 私密消息数据的几种情况：

//	1、私密消息
{
	'Type': 'PrivateMsg', 
	'FromQQ': {
		'UIN': 465152177, 
		'NickName': '\\u2660\\u2665\\u2663\\u2666'
	}, 
	'LogonQQ': 3501530063, 
	'TimeStamp': {
		'Recv': 1597152569, 
		'Send': 1597152569
	}, 
	'FromGroup': {
		'GIN': 0
	}, 
	'Msg': {
		'Req': 144, 
		'Seq': 72057596593849897, 
		'Type': 166, 
		'SubType': 134, 
		'SubTempType': 0, 
		'Text': '你好', 
		'BubbleID': 2561
	}, 
	'Hb': {
		'Type': 0
	}, 
	'File': {
		'ID': '', 
		'MD5': '', 
		'Name': '', 
		'Size': 0
	}
}

//	2、私密消息+图像信息
{
	'Type': 'PrivateMsg', 
	'FromQQ': {
		'UIN': 465152177, 
		'NickName': '\\u2660\\u2665\\u2663\\u2666'
	}, 
	'LogonQQ': 3501530063, 
	'TimeStamp': {
		'Recv': 1597152763, 
		'Send': 1597152763
	}, 
	'FromGroup': {
		'GIN': 0
	}, 
	'Msg': {
		'Req': 145, 
		'Seq': 72057594326773312, 
		'Type': 166, 
		'SubType': 134, 
		'SubTempType': 0, 
		'Text': '你好[pic,hash=0C29F0C67B0D61236A3AB0C6C9C0F04C,guid=/465152177-1250188513-0C29F0C67B0D61236A3AB0C6C9C0F04C]', 
		'BubbleID': 2561
	}, 
	'Hb': {
		'Type': 0
	}, 
	'File': {
		'ID': '', 
		'MD5': '', 
		'Name': '', 
		'Size': 0
	}
}


//	3、图像信息
{
	'Type': 'PrivateMsg', 
	'FromQQ': {
		'UIN': 465152177, 
		'NickName': '\\u2660\\u2665\\u2663\\u2666'
	}, 
	'LogonQQ': 3501530063, 
	'TimeStamp': {
		'Recv': 1597152849, 
		'Send': 1597152849
	}, 
	'FromGroup': {
		'GIN': 0
	}, 
	'Msg': {
		'Req': 146, 
		'Seq': 72057597158960012, 
		'Type': 166, 
		'SubType': 134, 
		'SubTempType': 0, 
		'Text': '[pic,hash=0C29F0C67B0D61236A3AB0C6C9C0F04C,guid=/465152177-3091349189-0C29F0C67B0D61236A3AB0C6C9C0F04C]', 
		'BubbleID': 2561
	}, 
	'Hb': {
		'Type': 0
	}, 
	'File': {
		'ID': '', 
		'MD5': '', 
		'Name': '', 
		'Size': 0
	}
}

// 群消息数据的几种情况：

//	1、群消息
{
	'Type': 'GroupMsg', 
	'FromQQ': {
		'UIN': 465152177, 
		'Card': '扑克-Float_Dream', 
		'SpecTitle': '', 
		'Pos': {
			'Lo': 2561, 
			'La': 0
		}
	}, 
	'LogonQQ': 3501530063, 
	'TimeStamp': {
		'Recv': 1597152675, 
		'Send': 1597152675
	}, 
	'FromGroup': {
		'GIN': 789235279, 
		'name': 'FloatDream氏族交流群'
	}, 
	'Msg': {
		'Req': 20756, 
		'Random': 1338084310, 
		'SubType': 134, 
		'AppID': 0, 
		'Text': '机器人测试', 
		'Text_Reply': '', 
		'BubbleID': 4
	}, 
	'File': {
		'ID': '', 
		'MD5': '', 
		'Name': '', 
		'Size': 17179869184
	}
}

//	2、图像信息
{
	'Type': 'GroupMsg', 
	'FromQQ': {
		'UIN': 465152177, 
		'Card': '扑克-Float_Dream', 
		'SpecTitle': '', 
		'Pos': {
			'Lo': 2561, 
			'La': 0
		}
	}, 
	'LogonQQ': 3501530063, 
	'TimeStamp': {
		'Recv': 1597152925, 
		'Send': 1597152925
	}, 
	'FromGroup': {
		'GIN': 789235279, 
		'name': 'FloatDream氏族交流群'
	}, 
	'Msg': {
		'Req': 20760, 
		'Random': 2809247917, 
		'SubType': 134, 
		'AppID': 0, 
		'Text': '[pic,hash=696B982AF60CF36016F204A829A24FDA]', 
		'Text_Reply': '', 
		'BubbleID': 4
	}, 
	'File': {
		'ID': '', 
		'MD5': '', 
		'Name': '', 
		'Size': 17179869184
	}
}

//	3、@成员+群消息
{
	'Type': 'GroupMsg', 
	'FromQQ': {
		'UIN': 465152177, 
		'Card': '扑克-Float_Dream', 
		'SpecTitle': '', 
		'Pos': {
			'Lo': 2561, 
			'La': 0
		}
	}, 
	'LogonQQ': 3501530063, 
	'TimeStamp': {
		'Recv': 1597153017, 
		'Send': 1597153017
	}, 
	'FromGroup': {
		'GIN': 789235279, 
		'name': 'FloatDream氏族交流群'
	}, 
	'Msg': {
		'Req': 20761, 
		'Random': 1604150205, 
		'SubType': 134, 
		'AppID': 0, 
		'Text': '[@3501530063] 测试', 
		'Text_Reply': '', 
		'BubbleID': 4
	}, 
	'File': {
		'ID': '', 
		'MD5': '', 
		'Name': '', 
		'Size': 17179869184
	}
}

//	4、@成员+群消息+图像信息


//	5、@成员+图像信息

//	6、@成员+无任何消息