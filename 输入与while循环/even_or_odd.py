# 奇数还是偶数
number = input("输入一个数字，我会告诉你它是偶数还是奇数：")
number = int(number)

if number % 2 == 0:
    print(f"\n这个数字{number}是偶数")
else:
    print(f"\n这个数字{number}是奇数")
