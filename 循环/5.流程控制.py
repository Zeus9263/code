# 流程控制


# 流程也就是计算机执行的顺序 顺序结构 分支结构 循环结构
# 分支结构: 单项分支 双向分支 多项分支
# 单项分支
# 程序员的女朋友给程序员打电话说 晚上下班回来的路上买10个包子，如果有看到卖西瓜的就买一个
baozi = 10
mxg = True
# 判断是否有卖西瓜的
if mxg :
    baozi = 1 # 单项分支结构
# print(baozi)
# 双向分支
if mxg:
    baozi = 2
else:
    baozi = 1

# 多向分支

# score = int(input())
# if score >=90 and score <=100:
#     print('A')
# elif score >= 80 and score < 90:
#     print('B')
# elif score >= 70 and score < 80:
#     print('C')
# elif score >= 60 and score < 70:
#     print('D')
# else:
#     print("WOW")


# 巢状分支 :在分支结构中 嵌套分支

'''
if 表达式a:
    if表达式b:
        if表达式c:
            ...
'''

# 练习题
'''
练习：要求输入一个四位数的年，判断当前的年份的生肖

生肖纪年顺序为：子鼠、丑牛、寅虎、卯兔、辰龙、巳蛇、午马、未羊、申猴、酉鸡、戌狗、亥猪


'''
year = int(input("请输入四位数的年份:"))
print(year)
if(year - 3) % 12 == 0 :
    print("猴年")
elif (year - 3) % 12 == 1:
    print("鸡年")
elif (year - 3) == 2:
    print("狗年")
elif (year - 3) % 12 == 3:
    print("猪年")
elif (year - 3) % 12 == 4:
    print("鼠年")
elif (year - 3) % 12 == 5:
    print("牛年")
elif (year - 3) % 12 == 6:
    print("虎年")
elif (year -3) % 12 == 7:
    print("兔年")
elif (year - 3) % 12 == 8:
    print("龙年")
elif (year - 3) % 12 == 9:
    print("蛇年")
elif (year - 3) % 12 == 10:
    print("马年")
elif (year - 3) % 12 == 11:
    print("羊年")
else :
    print("输入错误")

# year = int(input('输入一个四位数的年份:'))
# print(year)
# varlist = ['申猴','酉鸡','戌狗','亥猪','子鼠','丑牛','寅虎','卯兔','辰龙','巳蛇','午马','未羊']
# print(varlist[year%12])