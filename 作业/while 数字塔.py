outer = 1
while outer <= 6:
    inner = outer
    pos = 6       # create a position variable and start from 6 since you are printing backward
    while pos >= 1:
        if pos > inner:
            print(" ", end=" ")
            pos = pos - 1
        else:
            print(inner, end = " ")
            inner = inner - 1
            pos = pos - 1
    print(" ")
    outer = outer + 1