import os
import shutil

path = 'test1'  # 文件夹路径
path1 = 'test2'
opath = './test1/a1.txt'
npath = '.test2/a2.txt'
filename = './test1/a1.txt'
print(os.path.exists(path))  # 判断文件夹是否存在
os.mkdir(path)  # 创建文件夹
os.mkdir(path1)  # 创建文件夹
with open(filename, 'w') as file_object:
    file_object.write("test a1")
filename1 = './test2/a2.txt'
with open(filename1, 'w') as file_object:
    file_object.write("write a2")

# shutil.copyfile(opath, npath)
# print(os.path.exists(path))
