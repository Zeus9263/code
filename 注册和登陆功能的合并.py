# 注册和登陆功能的合并

# 专门定义数据变量,存放已经注册的用户信息
userlist = []  # 列表存放用户名
pwdlist = []  # 列表存放密码
blacklist = []  # 列表存放所有的黑名单用户

# 读取所有数据的方法
def readallusers():
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


# 封装一个函数 完成注册功能模块
def register():
    # 定义一个变量 用于控制外循环
    site = True
    # 循环执行 用户名输入操作
    while site:
        username = input("欢迎注册，请输入用户名:")  # 输入用户名

        # 用户名需要检测是否存在
        if username in userlist:
            print("当前用户名存在,请更换")
        else:
            while True:  # 循环输入密码 如果都正确 循环结束
                pwd = input("请输入密码:")  # 输入密码
                if len(pwd) >= 3:  # 检测密码长度
                    repwd = input("请输入确认密码:")  # 重复密码
                    if repwd == pwd:
                        # 用户名和密码都正确 都可以写入文件
                        # 打开文件 写入数据
                        with open('./user.txt', 'a+', encoding='utf-8') as fp:
                            fp.write(f'{username}:{pwd}\n') # 按照用户名:密码格式
                            # 结束外循环
                            site = False
                        break  # 结束内循环
                    else:
                        print("两次密码输入不一致,请重新输入")
                else:
                    print("密码格式错误,请重新输入")


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


# 判断当前的脚本是否作为一个主进程脚本在执行
if __name__ == '__main__':
    # 这里的代码只有在使用Python解释器直接运行时才会运行
    # 如果当前的脚本，作为了一个模块被其他的文件导入后使用，那么这里的代码不会执行
    # 因此，这里的代码，适合写当前脚本中的一些测试，这样不会影响其他脚本

    # 调用初始化方法 加载数据
    readallusers()

    while True:
        vars = '''
        **********************************
        **  登录(1)  注册(2) 退出(任意内容) **
        **********************************
        '''
        print(vars)

        # 让用户选择对应的操作

        num = input('请选择对应的序号，体验功能:')
        if num =='1':
            login()
        elif num =='2':
            register()
        else:
            print("欢迎下次体验....")
            break