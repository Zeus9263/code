# 10的整倍数
num = input("请输入一个数查看是否是10的整倍数")
num = int(num)
if num % 10 == 0:
    print(f"这个数字:{num} 是10的整倍数")
else:
    print(f"这个数字:{num} 不是10的整倍数")