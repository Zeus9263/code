# 后缀移动文件
import os
import glob
import shutil

path = r'F:\video\2022-4-24\照片'     #原始文件路径
path_new = r'F:\video\2022-4-24\img'   #目标文件路径
list_name = os.listdir(path)
print(list_name)
print(len(list_name))

for f in os.listdir(path):
    filename = os.path.join(path, f)
    if f.split(".")[-1] == "JPG":
        print(f)
        shutil.copy(filename, path_new)
print("done")

