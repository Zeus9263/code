current_users=['John','Sona','Angela','Luna','Civier']

new_users=['John','sona','Lisa','Tracy','Mike']

lower_current_users=[]

for user in current_users:
    lower_current_users.append(user.lower()) # 把现有的用户名都转换成小写追加到列表
# print(lower_current_users)
for user in new_users:
    if user.lower() in lower_current_users:
        print(f"{user},try another name!")
    else:
        print("Congratulations ,you can use "+user+" as your username!")
