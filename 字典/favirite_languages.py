# 调查编程语言
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")
for name, language in favorite_languages.items():
    # 需要包含字典名和方法items()
    # 他返回一个键值对列表
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys(): # keys() 将更好的被理解为键
    print(f"{name.title()}")

i = {'jin', 'jack','phil','edward','sarah','jen'}

for name in i:
    if name in favorite_languages.keys():
        print("Thank you",name)
    else:
        print("想来参加问卷调查么",name)
