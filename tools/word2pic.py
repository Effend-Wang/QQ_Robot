'''

该模块用于将文字转换为图片

模块需输入转换的文字
模块输出转换后图片在本地的缓存路径，路径暂时一律定为/buffer/w2p.png

TO DO：由于可能存在图片存储的冲突，因此需考虑使用其它命名办法存储并需对旧图片定时清理

'''

# 导入第三方库
from PIL import Image,ImageFont,ImageDraw
import os
import textwrap

# 转换文字为图片，返回图片绝对路径/buffer/w2p.png
def w2p(text):

	# 文字自动换行
	sptext=text.split("\n")
	hlen=len(sptext)
	for i in range(hlen):
		sptext[i]="\n".join(textwrap.wrap(sptext[i],width=35))
	text="\n".join(sptext)

	# 获取文字列表的最大字符数量
	max_len=0
	for item in text.split("\n"):
		if len(item)>max_len:
			max_len=len(item)

	# 转换文字为图片并保存为图片
	h=26*len(text.split("\n"))+10
	w=int(max_len*19.5+10)
	im=Image.new("RGB",(w,h),(255, 255, 255))
	dr=ImageDraw.Draw(im)
	fpath=os.getcwd()+"/data/fonts/msyh.ttf"
	font=ImageFont.truetype(fpath, 20)
	dr.text((5,5),text,font=font,fill="#000000")

	# 存储图片到本地路径/buffer/w2p.png
	save_path=os.getcwd()+"/buffer"
	if (os.path.exists(save_path)):
		save_path=save_path+"/w2p.png"
	else:
		os.mkdir(save_path)
		save_path=save_path+"/w2p.png"
	im.save(save_path)

	return save_path