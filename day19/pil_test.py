# !/usr/bin/env python
# coding=utf-8

import Image,ImageFilter

# 打开一个jpg图像文件 
im = Image.open('F:\Python\example\day19\me.jpg')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w/2, h/2))
# 把缩放后的图像用jpeg格式保存:
im.save('F:/Python/example/day19/thumbnail.jpg', 'jpeg')

# 模糊图片
im2 = im.filter(ImageFilter.BLUR)
im2.save('F:/Python/example/day19/blur.jpg','jpeg')

imm = Image.open('F:/Python/example/day19/blur.jpg')
im3 = imm.filter(ImageFilter.BLUR)
im3.save('F:/Python/example/day19/blur2.jpg','jpeg')