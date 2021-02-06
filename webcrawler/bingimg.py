import requests
import urllib
from bs4 import BeautifulSoup
import os

# 初始化参数
cnbing="http://cn.bing.com"

# 读取网页数据并获得图片链接
def get_url():
	res=requests.get(cnbing)
	soup=BeautifulSoup(res.text,'html.parser').select('link')[0]
	img_url=soup.get('href')
	img_name=img_url.split('.')[1]
	img_url=cnbing+img_url
	# 将图片保存在本地
	#path=os.getcwd()+'/'+img_name+'.jpg'
	#urllib.request.urlretrieve(img_url,path)

	return img_url
