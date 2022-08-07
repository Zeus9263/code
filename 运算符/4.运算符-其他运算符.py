# 其他运算符

u = 'iloveyoutosimida'
u = ['love', 'to', 'you']
u = ('love', 'to', 'you')
u = {'love', 'to', 'you'}
# u = {1: 'love', 2: 'to', 3: 'you'}  # 如果是字典类型 只能检测 键
# print('love' in u) # 检测字符串love是否存在于u 变量中
# print('love' not in u)  # 检测love字符串是否 不存在于u变量中


# is , is not 检测两个变量是否引用了同一个对象
a = 10
b = 10
# print(id(a),id(b)) # id()函数用于获取对象内存地址
# print(a is b) # a 是否和 b引用的值是一样的 是则true 否false
# print(a is not b) # 检测a和b 引用的值是否不一样 ↑
a = 10 and (30 and 0 ) or 20 and 15 or 35
print(a)