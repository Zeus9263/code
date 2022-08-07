def main():
    vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    print("请输入一行字符串：")
    count = 0
    str = input()
    for i in str:
        if (i in vowel):
            count += 1
    print("元音字母个数为：%d " % count)


main()
