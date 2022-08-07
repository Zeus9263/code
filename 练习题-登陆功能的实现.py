# 登陆功能的实现

# 专门定义数据变量,存放已经注册的用户信息
userlist = []  # 列表存放用户名
pwdlist = []  # 列表存放密码
blacklist = []  # 列表存放所有的黑名单用户
with open('./user.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)  # 调整当前指针到文件开头
    res = fp.readlines()  # 按照每一行读取所有的用户数据
    for i in res:  # 循环读取的每一行数据
        r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123 strip 处理空白字符 包括换行
        arr = r.split(':')  # admin:123  ==> ['admin','123']
        userlist.append(arr[0])  # 把用户名追加到用户名列表中
        pwdlist.append(arr[1])  # 把密码追加到密码列表中

# 获取黑名单账户
with open('./black.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)
    res = fp.readlines()
    for i in res:
        blacklist.append(i.strip())


# 封装函数 实现登陆功能
def login():
    # print(userlist)
    # print(pwdlist)
    # 定义变量 控制一开始的外循环
    islogin = True
    # 定义变量 用户密码的错误次数检测
    errornum = 3
    while islogin:
        # 获取登陆时的用户名
        username = input('欢迎登陆，请输入您的用户名:')
        # 检测当前用户是否存在
        if username in userlist:
            # 检测当前用户是否被锁定 判断是否在黑名单中
            if username in blacklist:
                print('当前用户处于锁定状态，不可登陆')
            else:
                # 定义循环 执行密码输入
                while True:
                    # 让用户输入密码
                    pwd = input('请输入您的密码')
                    # 获取用户名在用户列表中的索引
                    inx = userlist.index(username)
                    if pwd == pwdlist[inx]:
                        print('登陆成功')
                        # 结束循环
                        islogin = False  # 结束外循环变量
                        break
                    else:
                        # 密码错误则修改errornum次数变量
                        errornum -= 1
                        # 判断当前的密码错误次数 == 0
                        if errornum == 0:
                            # 如何才能锁定账户信息
                            with open('./black.txt', 'a+', encoding='utf-8') as fp:
                                fp.write(username + '\n')
                            print('曾经有那么几次机会摆在你的面前，你没有把握住，恭喜你，成功锁定了你的账户，请联系相关人员进行忏悔吧')
                            islogin = False  # 结束外循环变量
                            break
                        print(f'密码错误，请重新输入密码,您还有{errornum}次机会')
        else:
            # 用户名不存在
            print('用户名不存在,请重新输入')


login()
