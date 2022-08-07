# 注册功能

# 专门定义数据变量,存放已经注册的用户信息
userlist = []  # 列表存放用户名
pwdlist = []  # 列表存放密码

with open('./user.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)  # 调整当前指针到文件开头
    res = fp.readlines()  # 按照每一行读取所有的用户数据
    for i in res:  # 循环读取的每一行数据
        r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123 strip 处理空白字符 包括换行
        arr = r.split(':')  # admin:123  ==> ['admin','123']
        userlist.append(arr[0])  # 把用户名追加到用户名列表中
        pwdlist.append(arr[1])  # 把密码追加到密码列表中


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


register()
