# 密码破解
import time
import itertools
# mylist = list(itertools.product("0123456789", repeat=10))
passwd = ("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm", repeat=6))
# print(mylist)
# print(len(mylist))
while True:
    #先直接实现，然后再添加异常
    try:
        str = next(passwd)
        time.sleep(0.5)
        print(str)
    except StopIteration as e:
        break
