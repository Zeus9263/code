# squares
squares = []
for value in range(1,11):
    square = value ** 2 # ②
    squares.append(square) # ③
print(squares)
squares = []
for value in range(1,11):
    squares.append(value**2) # ① 处的代码与 ② ③处的代码等效
    # 在循环中 计算每个值的平方 并立即将结果附加到列表squares的末尾
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
# 列表解析 将for循环和创建新元素的代码合并成一行 并自动附加新元素
print(squares)