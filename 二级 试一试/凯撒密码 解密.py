# 凯撒密码解密
# 凯撒密码 实现加密与解密
password=input("请输入密文文本")
for p in password:
    if "a"<=p<="z":
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26),end="")
    elif "A"<=p<="Z":
        print(chr(ord("A")+(ord(p)-ord("Z")-3)%26),end="")
    else:print(p,end="")