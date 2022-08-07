# 访客名单
filename = 'guest_book.txt'


while 1:
    i = input("请输入名字\n")
    if i == 'q':
        break
    else:
        print("欢迎你{}".format(i))
        with open(filename, 'a') as f:
            f.write(i+'\n')