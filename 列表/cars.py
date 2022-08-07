# cars 车
cars = ['bmw','audi','toyota','sabaru']
# sort() 按字母顺序排序
# cars.sort()
print(cars)

# cars.sort(reverse=True)
# 还可以按与字母顺序相反的顺序排列列表元素
# 只需向sort()方法传递参数reverse=True即可
# 对列表元素排列顺序的修改是永久性的
# print('Here is the original list')
# print(cars)
#
# print('\nHere is the sorted list')
# print(sorted(cars))
# sorted 函数能让你按特定顺序显示列表元素 不影响他们在列表中的原始排列顺序
# 如果要按字母顺序相反的顺序显示列表 也可向sortd()函数传递reverse=True
# print('\nHere is the original list again:')
# print(cars)

cars.reverse()
print(cars)
# 方法reverse() 永久性的修改列表元素的排列顺序
# 但可随时恢复到原来的排列数序 只需要对列表再次调用 reverse() 即可

# 使用len()函数可以快速获取列表的长度
print(len(cars))
