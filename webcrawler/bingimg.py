'''

该模块用于爬取必应图片搜索网页上的图片

模块需要输入需要搜索的内容
模块返回随机图片的url，随机前100张图片

'''

# 导入第三方库
import random
import os
import requests
import urllib
from bs4 import BeautifulSoup
from json import loads

bingimgurl="https://cn.bing.com/images/"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

def get_url(message):
	search=message.split(" ",1)[1]
	randint=random.randint(1,100)
	requrl=bingimgurl+"async?q="+search.replace(" ","")+"&first="+str(randint)+"&tsc=ImageBasicHover"
	res=requests.get(requrl,headers=headers)
	soup=BeautifulSoup(res.text,'html.parser')
	m=soup.find("a",class_="iusc").get("m")
	m=loads(m)
	imgurl=m.get("murl")

	return imgurl