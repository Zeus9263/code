# 循环结构

# num = 1
# while num <= 10: # 循环 判断当前条件是否成立
#     # 将要执行代码
#     print(num)
#     num += 1 # 更改变量 目的是为了进行下一步 并且是要朝着循环结束的方向发展

# for 循环 通常 for循环用来遍历一个容器类型的数据

vars = '123456789'
# vars = ['a,b,c,d,e,f,g']
# 使用for in 循环 遍历容器类型数据 那么中间的i 变量就是当前容器类型中的每一个元素
for i in vars:
    print(i)


for i in range(1,10):
    print(i,u'*'*hash(2),end=(" "))
