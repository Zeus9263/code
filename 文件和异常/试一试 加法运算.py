# 加法运算
while True:
    number_a = input('请输入一个数字：')
    number_b = input('请输入另一个数字：')
    try:
        #ValueError错误处理 原题给出的是TypeError无法处理
        numuber_sum = int(number_a) + int(number_b)
        print('您输入的两个数字之和为：'+str(numuber_sum))
    except ValueError:
        print('抱歉，您输入的不是两个数字！')
