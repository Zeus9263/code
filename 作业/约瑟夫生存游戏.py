list = list(range(1, 31))
countNum = 1
for i in list:
    if countNum <= 15:
        print("{}号下船了".format(list[8]))
        list = list[9:] + list[:8]
    countNum += 1
