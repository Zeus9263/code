# 批量重命名文件
import os

# 文件路径
path = 'G:/新建文件夹/新建文件夹'
# 计数器num
num = 1
# 文件循环
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, str(num) + ".mp3"))
    # 更名
    num += 1
print("------------命名完成------------")
