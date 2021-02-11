'''

该文档用于腾讯智能对话平台TBP应用接入和处理
TBP使用HTTPS协议通信，使用签名方法v3（TC3-HMAC-SHA256）
实际使用的签名密钥通过数据库读取和存储，不于实际代码中显示以保证密钥安全性
数据库字段格式：<botname>,<type>,<botid>,<secretid>,<secretkey>
botname为Bot名称，type为签名方法，botid为TBP的botid，secretid为签名，secretkey为签名密钥
TBP CDK第三方运行库: tencentcloud-sdk-python

'''

# 导入第三方库
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tbp.v20190627 import tbp_client, models

# 导入程序模块
import database_operate
import tencent_cloud.tencent_globalvar as tencent_globalvar

# 初始化
tbp_url="tbp.tencentcloudapi.com"

# 发送TBP请求获得数据并处理
def get_tbpchat(message_from_user):

	message_from_user=message_from_user.split(" ",1)

	# 获取密钥
	tbp_signature=tencent_globalvar.get_tencent_list("tbp_signature")
	botname=tbp_signature[0][0]
	secrettype=tbp_signature[0][1]
	botid=tbp_signature[0][2]
	secretid=tbp_signature[0][3]
	secretkey=tbp_signature[0][4]

	# 创建通信
	cred=credential.Credential(secretid,secretkey)
	httpProfile=HttpProfile()
	httpProfile.endpoint=tbp_url

	clientProfile=ClientProfile()
	clientProfile.httpProfile=httpProfile
	client=tbp_client.TbpClient(cred,"",clientProfile)

	req=models.TextProcessRequest()
	params={
		"BotId":botid,
		"BotEnv":"release",
		"TerminalId":"v1",
		"InputText":message_from_user[1]
	}
	req.from_json_string(json.dumps(params))
	resp=client.TextProcess(req)

	# 格式化接收到的数据
	resp=json.loads(str(resp))
	message_to_send=resp.get("ResponseMessage").get("GroupList")[0].get("Content")

	return message_to_send