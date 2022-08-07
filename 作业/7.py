l = []
for i in range(1, 101):
    if i % 7 == 0:
        l.append(i)
    elif str(i)[-1] == '7':
        l.append(i)
print(l)