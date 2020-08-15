# QQ_Robot
该机器人由开发者Effend Wang编写。
版本号：v0.4
发布日期：2020.08.16

改动信息：改动程序整体框架，引入数据库存储与操作功能，添加管理员操作数据库功能。

额外信息：无。

API及框架说明：
（1）由于酷Q已经不再提供服务，因此改用小栗子框架运行；
（2）机器人的用户手册以及程序的开发手册均位于Docs；
（3）酷Q框架API示例位于CQ API Examples；
（4）Warframe API示例位于warframe/Warframe API Examples；
（5）Warframe Market API示例位于warframe/WM API Examples；
（6）warframe翻译文档示例位于warframe/Translation Examples；
（7）小栗子xzfg API示例位于xzfg API Examples；

注意事项：
（1）为避免信息泄露，已将所有含有私密信息的内容改为需要自行添加的文件。
（2）用户文档及开发文档由于开发时效原因可能存在错漏，还请谅解。
（3）在chat_authority.py中控制聊天权限，需要自行设置，相关设置要求查看代码文件注释部分。
（4）roboy.py中__main__的定义中需要设置从框架接收事件的端口。

机器人程序概要：
（1）机器人采用flask模块对框架上报事件的端口进行监听，在同一个窗口下进行数据处理和回复，因此对于大量数据的处理能力可能较弱，受到框架能力的影响。
（2）通过chat_authority.py对聊天权限进行控制，由于程序的整合性，存在权限的优先级，需根据需求在send_message.message_creat()中更改优先级。
（3）所有需进行提取的数据均由access database构成，文件名为.mdb，数据文件均位于/data。
（4）通过管理员权限，可对/data下的部分数据库进行增、查操作（删、改操作暂未编写完成）。

需自行添加的文件：
（1）在/data/config下需添加authority.mdb数据库文件，其中保存聊天权限的设置，具体文件格式及内容在chat_authority.py中可以看到。
（2）在/data/config下需添加self_id.txt文件，其中保存机器人QQ号，仅可保存单个号码且不包含其它任何内容。

已提供和未来将提供的功能有：
（1）Warframe国际服：
1、查询游戏实时信息；
2、查询Warframe Market实时交易信息；
3、游戏内容翻译；
4、查询Warframe Wiki内容（暂未开发）；
（2）崩坏三国服（暂未开发）：
（3）机器人管理员：
1、数据库操作；
（4）腾讯AI聊天（暂未开发）：

