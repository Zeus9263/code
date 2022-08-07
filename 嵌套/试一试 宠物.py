# 宠物 pets
pet1 = {'name': 'labrador', 'master': 'jack'}
pet2 = {'name': 'husky', 'master': 'lat'}
pet3 = {'name': 'blueCat', 'master': 'kaw'}
pet4 = {'name': 'siameseCat', 'master': 'saq'}
pets = [pet1, pet2, pet3, pet4]
for pet in pets:
    print(f"宠物的类型是:{pet['name']}\n主人是:{pet['master']}")