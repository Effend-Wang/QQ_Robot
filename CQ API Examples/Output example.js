// 私密消息数据的几种情况：

//	1、私密消息
{
	'font': 44749224, 
	'message': [
		{
			'data': {
				'text': '你好'
			}, 
			'type': 'text'
		}
	], 
	'message_id': 85, 
	'message_type': 'private', 
	'post_type': 'message', 
	'raw_message': '你好', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'nickname': '♠♥♣♦', 
		'sex': 'male', 
		'user_id': 465152177
	}, 
	'sub_type': 'friend', 
	'time': 1595413286, 
	'user_id': 465152177
}

//	2、私密消息+图像信息

{
	'font': 44749224, 
	'message': [
		{
			'data': {
				'text': '你好'
			}, 
			'type': 'text'
		}, 
		{
			'data': {
				'file': 'E878A02E755E9F497E09B6B015BE5AD9.jpg', 
				'url': 'https://c2cpicdw.qpic.cn/offpic_new/465152177//465152177-2995598441-E878A02E755E9F497E09B6B015BE5AD9/0?term=2'
			}, 
			'type': 'image'
		}
	], 
	'message_id': 86, 
	'message_type': 'private', 
	'post_type': 'message', 
	'raw_message': '你好[CQ:image,file=E878A02E755E9F497E09B6B015BE5AD9.jpg]', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'nickname': '♠♥♣♦', 
		'sex': 'male', 
		'user_id': 465152177
	}, 
	'sub_type': 'friend', 
	'time': 1595413331, 
	'user_id': 465152177
}

{
	'font': 91271360, 
	'message': [
		{
			'data': {
				'file': 'E878A02E755E9F497E09B6B015BE5AD9.jpg', 
				'url': 'https://c2cpicdw.qpic.cn/offpic_new/465152177//465152177-2995598441-E878A02E755E9F497E09B6B015BE5AD9/0?term=2'
			},
			'type': 'image'
		},
		{
			'data': {
				'text': '你好'
			},
			'type': 'text'
		}
	],
	'message_id': 87, 
	'message_type': 'private', 
	'post_type': 'message', 
	'raw_message': '[CQ:image,file=E878A02E755E9F497E09B6B015BE5AD9.jpg]你好', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'nickname': '♠♥♣♦', 
		'sex': 'male', 
		'user_id': 465152177
	}, 
	'sub_type': 'friend', 
	'time': 1595413349, 
	'user_id': 465152177
}

//	3、图像信息
{
	'font': 91271360, 
	'message': [
		{
			'data': {
				'file': 'FF6E973657CD3CB2CB2252D17404006D.png', 
				'url': 'https://c2cpicdw.qpic.cn/offpic_new/465152177//465152177-4267276573-FF6E973657CD3CB2CB2252D17404006D/0?term=2'
			}, 'type': 'image'
		}
	], 
	'message_id': 88, 
	'message_type': 'private', 
	'post_type': 'message', 
	'raw_message': '[CQ:image,file=FF6E973657CD3CB2CB2252D17404006D.png]', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'nickname': '♠♥♣♦', 
		'sex': 'male', 
		'user_id': 465152177
	}, 
	'sub_type': 'friend', 
	'time': 1595413364, 
	'user_id': 465152177
}

// 群消息数据的几种情况：

//	1、群消息
{
	'anonymous': None, 
	'font': 44749672, 
	'group_id': 608634144, 
	'message': [
		{
			'data': {
				'text': 'emmmm'
			}, 
			'type': 'text'
		}
	], 
	'message_id': 89, 
	'message_type': 'group', 
	'post_type': 'message', 
	'raw_message': 'emmmm', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'area': '武汉', 
		'card': '未来是多久', 
		'level': '律者的黄昏', 
		'nickname': '♠♥♣♦', 
		'role': 'owner', 
		'sex': 'male', 
		'title': '', 
		'user_id': 465152177
	}, 
	'sub_type': 'normal', 
	'time': 1595413391, 
	'user_id': 465152177
}

//	2、图像信息
{
	'anonymous': None, 
	'font': 91271744, 
	'group_id': 608634144, 
	'message': [
		{
			'data': {
				'file': '78BA07D9F137BA1752A0768F1E0DF643.jpg', 
				'url': 'https://gchat.qpic.cn/gchatpic_new/465152177/608634144-2644664581-78BA07D9F137BA1752A0768F1E0DF643/0?term=2'
			}, 
			'type': 'image'
		}
	], 
	'message_id': 90, 
	'message_type': 'group', 
	'post_type': 'message', 
	'raw_message': '[CQ:image,file=78BA07D9F137BA1752A0768F1E0DF643.jpg]', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'area': '武汉', 
		'card': '未来是多久', 
		'level': '律者的黄昏', 
		'nickname': '♠♥♣♦', 
		'role': 'owner', 
		'sex': 'male', 
		'title': '', 
		'user_id': 465152177
	}, 
	'sub_type': 'normal', 
	'time': 1595413407, 
	'user_id': 465152177
}

//	3、@成员+群消息
{
	'anonymous': None, 
	'font': 44749384, 
	'group_id': 608634144, 
	'message': [
		{
			'data': {
				'qq': '3501530063'
			}, 
			'type': 'at'
		}, 
		{
			'data': {
				'text': ' 测试'
			}, 
			'type': 'text'
		}
	], 
	'message_id': 91, 
	'message_type': 'group', 
	'post_type': 'message', 
	'raw_message': '[CQ:at,qq=3501530063] 测试', 
	'self_id': 3501530063, 
	'sender': {
		'age': 24, 
		'area': '武汉', 
		'card': '未来是多久', 
		'level': '律者的黄昏', 
		'nickname': '♠♥♣♦', 
		'role': 'owner', 
		'sex': 'male', 
		'title': '', 
		'user_id': 465152177
	}, 
	'sub_type': 'normal', 
	'time': 1595413436, 
	'user_id': 465152177
}

//	4、@成员+群消息+图像信息
{
	'anonymous': None, 
	'font': 91271008, 
	'group_id': 608634144, 
	'message': [{'data': {'qq': '3501530063'}, 'type': 'at'}, {'data': {'text': ' 测试'}, 'type': 'text'}, {'data': {'file': 'F13C1F8C9C44490671962A5697EDAEE5.png', 'url': 'https://gchat.qpic.cn/gchatpic_new/465152177/608634144-2546113351-F13C1F8C9C44490671962A5697EDAEE5/0?term=2'}, 'type': 'image'}], 
	'message_id': 92, 
	'message_type': 'group', 
	'post_type': 'message', 
	'raw_message': '[CQ:at,qq=3501530063] 测试[CQ:image,file=F13C1F8C9C44490671962A5697EDAEE5.png]', 'self_id': 3501530063, 'sender': {'age': 24, 'area': '武汉', 'card': '未来是多久', 'level': '律者的黄昏', 'nickname': '♠♥♣♦', 'role': 'owner', 'sex': 'male', 'title': '', 'user_id': 465152177}, 
	'sub_type': 'normal', 
	'time': 1595413465, 
	'user_id': 465152177
}

//	5、@成员+图像信息
{'anonymous': None, 'font': 44749352, 'group_id': 608634144, 'message': [{'data': {'qq': '3501530063'}, 'type': 'at'}, {'data': {'text': ' '}, 'type': 'text'}, {'data': {'file': '696B982AF60CF36016F204A829A24FDA.jpg', 'url': 'https://gchat.qpic.cn/gchatpic_new/465152177/4126915435-2632517409-696B982AF60CF36016F204A829A24FDA/0?term=2'}, 'type': 'image'}], 'message_id': 93, 'message_type': 'group', 'post_type': 'message', 'raw_message': '[CQ:at,qq=3501530063] [CQ:image,file=696B982AF60CF36016F204A829A24FDA.jpg]', 'self_id': 3501530063, 'sender': {'age': 24, 'area': '武汉', 'card': '未来是多久', 'level': '律者的黄昏', 'nickname': '♠♥♣♦', 'role': 'owner', 'sex': 'male', 'title': '', 'user_id': 465152177}, 'sub_type': 'normal', 'time': 1595413485, 'user_id': 465152177}

//	6、@成员+无任何消息
{'anonymous': None, 'font': 44749352, 'group_id': 608634144, 'message': [{'data': {'qq': '3501530063'}, 'type': 'at'}], 'message_id': 94, 'message_type': 'group', 'post_type': 'message', 'raw_message': '[CQ:at,qq=3501530063]', 'self_id': 3501530063, 'sender': {'age': 24, 'area': '武汉', 'card': '未来是多久', 'level': '律者的黄昏', 'nickname': '♠♥♣♦', 'role': 'owner', 'sex': 'male', 'title': '', 'user_id': 465152177}, 'sub_type': 'normal', 'time': 1595413500, 'user_id': 465152177}