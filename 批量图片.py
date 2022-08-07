# -*- coding: utf-8 -*-
# 批量图片

import os

from PIL import Image

# 获取图片在文件夹里的路径
fileName = os.listdir('C:\\Users\Zeus\Desktop\img\\')

# for img in fileName:
#     print('C:\\Users\Zeus\Desktop\img\\'+img)

# width = 400
# height = 400
# 创建一个新的文件夹
# 图片像素位置 box=普通大小 bigbox=放大一些
box = (0, 643, 1080, 1690)
bigbox = (0, 740, 1080, 1640)
os.mkdir('C:\\Users\Zeus\Desktop\we\\')
for img in fileName:
    pic = Image.open('C:\\Users\Zeus\Desktop\img\\' + img)
    newpic = pic.crop(box)
    print(newpic)
    # save 保存
    newpic.save('C:\\Users\Zeus\Desktop\we\\'+img)
print("------------保存完成------------")