# 访客
i = input("请输入名字")
filename = 'guest.txt'
with open(filename,'a') as f:
    f.write(i)