# 该文件代码用于全局数据库操作，包括查询、新增、删除、更新4个操作功能

import pypyodbc

def access_operate(operate,value,db_path):

	if operate=="query":
		result=access_query(db_path,value)
	elif operate=="add":
		result=access_add(db_path,value)
	elif operate=="delete":
		result=access_delete(db_path,value)
	elif operate=="update":
		set_value=value.split(2)[0]
		value=value.split(2)[1]
		result=access_update(db_path,set_value,value)
	#elif operate=="all":
		#result=access_all(db_path)

	return result

# 数据库查询，db_path为数据库路径，value为xxx=xxx and xxx=xxx格式
def access_query(db_path,value):
	try:
		db=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % db_path)
		cursor=db.cursor()
		command="SELECT * from data WHERE %s" %value
		result=[i for i in cursor.execute(command)]
		cursor.close()
		db.close()
		return result
	except:
		return []

# 数据库添加，db_path为数据库路径，value为'','',...格式
def access_add(db_path,value):
	try:
		db=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % db_path)
		cursor=db.cursor()
		command="INSERT INTO data VALUES%s" %value
		cursor.execute(command)
		cursor.commit()
		cursor.close()
		db.close()
		return True
	except:
		return False

def access_delete(db_path,value):
	try:
		db=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % db_path)
		cursor=db.cursor()
		command="DELETE FROM data WHERE %s" %value
		cursor.execute(command)
		cursor.commit()
		cursor.close()
		db.close()
		return True
	except:
		return False

def access_update(db_path,set_value,value):
	try:
		db=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % db_path)
		cursor=db.cursor()
		command="UPDATE data SET %s WHERE %s" %(set_value,value)
		cursor.execute(command)
		cursor.commit()
		cursor.close()
		db.close()
		return True
	except:
		return False

# 输出数据库的所有数据
# 注意：该功能不可于实际使用，可能因数据量过大导致问题，仅可用于本地测试
def access_all(db_path):
	try:
		db=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % db_path)
		cursor=db.cursor()
		command="SELECT * from data"
		result=[i for i in cursor.execute(command)]
		cursor.close()
		db.close()
		return result
	except:
		return []