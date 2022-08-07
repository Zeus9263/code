# 试一试 城市名
def city_country(city, country):
    cty = country + '，' + city
    return cty


c = city_country('成都', '中国')
print('---------------------\n')
print('"' + c + '"')
print('\n---------------------')
c = city_country('贵州', '中国')
print('---------------------\n')
print('"' + c + '"')
print('\n---------------------')
c = city_country('北京', '中国')
print('---------------------\n')
print('"' + c + '"')
print('\n---------------------')