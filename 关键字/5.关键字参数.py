#  关键字参数

# kw = keyword
def func(a,b,c=3,*args,name,age,**kwargs):
    print(a,b,c)
    print(args) # 普通参数收集 会把多余的参数收集成元组
    print(name,age)
    print(kwargs) # 关键字参数收集 会把多余的参数收集成为 字典

func(1,2,3,111,222,name='abc',age='123',i='abc',l='aaa',w='aw')

# 注意行参声明的位置
# 普通参数，默认参数，收集参数，关键字参数，关键字收集参数
'''
极小概率会出现上面五种行参
一般情况下： 普通参数 收集参数 关键字收集参数
'''