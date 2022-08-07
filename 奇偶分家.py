# 奇偶分家 给定N个正整数，请统计奇数和偶数各有多少个？
a = int(input())
suma = 0
sumb = 0
x = input().split()
for i in x:
    if int(i) % 2 == 1:
        suma += 1
    else:
        sumb += 1
print(suma, sumb)