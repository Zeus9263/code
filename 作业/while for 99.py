for i in range(1,10):
    for j in range(1,i+1):
        # \t 是制表符，用来对齐。end 默认是 \n，打印后会换行，end='' 可以防止换行
        print(str(j) + '×' + str(i) + '=' + str(i * j) + '\t', end='')
    # 打印完一行后换行
    print('')

