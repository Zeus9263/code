# Dict 字典类型

"""
    + 字典也是用于储存一组或者多组数据使用，用大括号{}来定义
    + 字典是 键值对 的储存方式 name:admin
    + 键值对之间用冒号分割，多组键值对之间用 , 逗号进行分割
    + 键必须是字符串或数字类型，值可以是任意类型
    + 键名不能重复，值可以重复
"""

# vard = {'title':'<<鬼谷子>>','author':'鬼谷子','price':'29.99'}

# print(vard,type(vard)) # type打印类型 <class 'dict'>

# 比如记录一本书的相关信息 书名 作者 价格
# 获取字典中的值
# vard = {'title':'<<鬼谷子>>','author':'鬼谷子','price':'29.99'}

# print(vard['title'])


vard = {'a': '10', 'b': '15', 'c': '20', '1': 'abcdef#', }

print(vard)

### tip: 在python之前的版本中 字典是无序的
