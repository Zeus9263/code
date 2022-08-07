import random

computer = random.randint(1, 100)
while True:
    number = int(input("请输⼊100以内的整数："))
    if (number > computer):
        print("⼤了")
    elif (number < computer):
        print("⼩了")
    else:
        print("恭喜你")
        break
