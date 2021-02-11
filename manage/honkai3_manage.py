'''

该模块提供针对honkai3特定的管理权限，权限名：honkai3_manage

可增添/修改内容有：
1、战场信息：新增战场/修改战场 <名称> <阵容1> <阵容2> ... <阵容10>
2、深渊信息：新增深渊/修改深渊 <名称> <阵容1> <阵容2> ... <阵容10>（暂不提供）

'''

# 导入第三方库
import os

# 导入程序模块
from honkai3.honkai3_globalvar import honkai3_db_loading
from honkai3.honkai3_globalvar import recent_change
import database_operate as dbop

db_honkai3={
	"honkai3_shenyuan":"/data/honkai3/shenyuan.mdb",
	"honkai3_zhanchang":"/data/honkai3/zhanchang.mdb"
}
key=["名称","阵容1","阵容2","阵容3","阵容4","阵容5","阵容6","阵容7","阵容8","阵容9","阵容10"]

# honkai3管理模块主程序
def honkai3_manage(message_from_user):
	message_to_send=""
	message_check=message_from_user.split()
	status=False

	if (message_check[0]=="修改战场"):
		status=update(message_from_user,os.getcwd()+db_honkai3.get("honkai3_zhanchang"))
		if status==False:
			message_to_send="数据修改失败，请检查请求格式"

	elif (message_check[0]=="新增战场"):
		status=add(message_from_user,os.getcwd()+db_honkai3.get("honkai3_zhanchang"))
		if status==False:
			message_to_send="数据新增失败，请检查请求格式"

	#elif (message_check[0]=="修改深渊"):
		#status=update(message_from_user,os.getcwd()+db_honkai3.get("honkai3_shenyuan"))
		#if status==False:
			#message_to_send="数据修改失败，请检查请求格式"

	#elif (message_check[0]=="新增深渊"):
		#status=add(message_from_user,os.getcwd()+db_honkai3.get("honkai3_shenyuan"))
		#if status==False:
			#message_to_send="数据新增失败，请检查请求格式"

	elif (message_check[0]=="修改当期战场"):
		recent_change("zhanchang",message_check[1])
		message_to_send="已修改当期战场"

	#elif (message_check[0]=="修改当期深渊"):
		#recent_change("shenyuan",message_check[1])
		#message_to_send="已修改当期深渊"

	elif (message_check[0]=="重载数据库"):
		honkai3_db_loading()
		message_to_send="崩坏三数据库已重载"

	return message_to_send

# 修改数据库数据
# 返回修改成功与否状态
def update(message_from_user,db_path):
	status=False
	value_where="名称='%s'" %(message_from_user.split()[1])
	values=message_from_user.split()[2:]
	for i in range(len(values)):
		values[i]=key[i]+"='"+values[i]+"'"
	set_value=",".join(values)

	status=dbop.access_update(db_path,set_value,value_where)

	return status

# 新增数据库数据
# 返回新增成功与否状态
def add(message_from_user,db_path):
	status=False
	values=message_from_user.split()[1:]
	for i in range(len(values)):
		values[i]="'"+values[i]+"'"
	value="("+",".join(values)+")"

	status=dbop.access_add(db_path,value)

	return status