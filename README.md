# QQ_Robot
该机器人由开发者Effend Wang编写。
版本号：v0.2
发布日期：2020.08.09

改动信息：改动部分warframe游戏数据查询输出信息

额外信息：完成warframe游戏数据的查询功能；完成warframe market物品交易查询功能；完成warframe游戏内容翻译功能

说明：
（1）该机器人需要在酷Q框架下运行，且需有一些特别的设定；
（2）机器人的用户手册以及程序的开发手册均位于Docs；
（3）框架API示例位于CQ API Example；
（4）程序测试用示例位于Test Example；
（5）Warframe API示例位于warframe/Warframe API Examples；
（6）Warframe Market API示例位于warframe/WM API Examples；
（7）warframe翻译文档示例位于warframe/Translation Examples；

注意事项：
（1）为避免信息泄露，已经将robot.py中的self_id值去除，需自行设置，数值格式为number。
（2）用户文档及开发文档由于开发时效原因可能存在错漏，还请谅解。
（3）在chat_authority.py中控制聊天权限，需要自行设置，相关设置要求查看代码文件注释部分。
（4）roboy.py中__main__的定义中需要设置从框架接收事件的端口。

机器人程序概要：
（1）机器人采用flask模块对框架上报事件的端口进行监听，在同一个窗口下进行数据处理和回复，因此对于大量数据的处理能力可能较弱，受到框架能力的影响。
（2）通过chat_authority.py对聊天权限进行控制，由于程序的整合性，存在权限的优先级，需根据需求在send_message.message_creat()中更改优先级。
（3）所有需进行提取的数据均由.py文件构成，暂未使用数据库形式保存。

已提供和未来将提供的功能有：
	（1）Warframe国际服：
		1、查询游戏实时信息；
		2、查询Warframe Market实时交易信息；
		3、游戏内容翻译；
		4、查询Warframe Wiki内容（暂未开发）；
	（2）崩坏三国服（暂未开发）：
	（3）机器人管理员（暂未开发）：
	（4）腾讯AI聊天（暂未开发）：
