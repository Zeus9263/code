# 跟管理员打招呼
users = ['admin','zeus','boos','visitor','loginUser']
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print(f"Hello {user},thank you for logging in again")

else:
    print("We need to find some users")
