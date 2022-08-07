# 试一试 放眼世界 想出5个你渴望想去旅游的地方

tourism = ['日本东京','中国西藏','韩国首尔','中国恩施','中国上海']
print(f'原始列表{tourism}')
# print(f'字母顺序排列{sorted(tourism)}')
# print(f'翻转顺序{sorted(tourism,reverse=True)}')
# tourism.reverse()
# print(f'使用reverse后{tourism}')
# tourism.reverse()
# print(f'再次使用reverse后{tourism}')
tourism.sort()
print(tourism)
tourism.sort(reverse=True)
print(tourism)

