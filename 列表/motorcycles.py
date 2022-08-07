# motocycles 摩托车
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# print(motorcycles)
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles[0])

motorcycles.append('ducati')
print(motorcycles)

# motorcycles.insert(0,'ducati')
# print(motorcycles)
#
# del motorcycles[0]
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# last_owned = motorcycles.pop() # pop 弹出
# print(f'The last motocycles I owned was a {last_owned.title()}')
#
#
# last_owned = motorcycles.pop(0) # pop 弹出
# print(f'The first motocycles I owned was a {last_owned.title()}')
motorcycles.remove('ducati') # remove 移除指定元素的值
print(motorcycles)