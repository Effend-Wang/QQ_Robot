'''
	
该模块用于引入本地类数据，包括：
1、用户图片存储操作；
2、用户笔记存储操作；
3、本地图片存储操作；
4、本地笔记存储操作；

用户相关数据文件均存放于/user下，文件作为永久性文件在程序中继承。
本地相关数据文件均存放于/data/local下，作为程序本地文件调用使用。

'''

import os
import 