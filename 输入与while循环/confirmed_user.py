# confirmen_user
unconfirmen_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户 直到没有未验证的用户为止
# 将每个经过验证的用户都移到已验证用户列表中
while unconfirmen_users:
    current_user = unconfirmen_users.pop()

    print(f"Verifying user: {confirmed_users}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for current_user in confirmed_users:
    print(current_user.title())