# !/usr/bin/env python
# coding=utf-8

import Image,ImageDraw,ImageFont,ImageFilter
import random

# 随机字母
def rndChar():
	return chr(random.randint(65,90))

# 随机颜色1
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色2
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 图片的宽高
width = 60*4
height = 60
# 创建图片对象
image = Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# 创建绘画对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
# 输出文字
for t in range(4):
	# 坐标、随机字符、字体、颜色填充
	draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

# 模糊处理
image = image.filter(ImageFilter.BLUR)
# 保存图片
image.save('code.jpg','jpeg')