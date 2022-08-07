# pi_string
# open
pi_string = ''
text_path = 'chapter_10/pi_digits.txt'
with open(text_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string)
print(len(pi_string))


file_path = 'chapter_10/pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


print(f'{pi_string[:52]}...')
print(len(pi_string))

birthday = input("输入你的生日 格式为yymmdd:")
if birthday in pi_string:
    print('你的生日存在于圆周率中')
else:
    print('你的生日不存在于圆周率前100万位中')
