# 数值比较
age = 18
print(age == 18)
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 检查多个条件
# 使用 and 检查多个条件
age_0 = 22
age_1 = 18
# if age_0 >= 2 and age_1 >= 21:
#     print(True)
# else:
#     print(False)
age_1 = 22
if age_0 >= 21 and age_1 >= 21: # 检查  变量age_0 和 age_1 是否都大于等于21
    print(True) # True
else:
    print(False) # False
# 使用 or 检查多个条件
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21: # 检查  变量age_0 和 age_1 其中一个是否大于等于21
    print(True) # True
else:
    print(False) # False
# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_toppings:
    print(True)
else:
    print(False)