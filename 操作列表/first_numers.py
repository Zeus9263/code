# 使用函数 range()
for value in range(1,5): # 上述代码看起开应该打印1-5 实际上只打印数字1-4
    print(value)
for value in range(1,6): # 要输出数字1-5 需要使用range(1,6)
    # 这样 输出将从1开始 到5结束
    print(value)
for value in range(6): # 调用函数range()时 也可以只指定一个参数 这样他将从0开始
    # 例如range(6)返回0-5
    print(value)
numbers = list(range(1,6))
print(numbers)
# 使用函数range()时 还可指定步长 为此 可以给这个函数指定第三个函数 ，python将根据这个步长来生成数
# 例如下面的代码打印 1-10的偶数
even_numbers = list(range(2,11,2))
print(even_numbers)
