# 试一试 邀请嘉宾
invitation = ['张三','李四','王五']
print(invitation)
invitable = invitation[2]
print(f'{invitable}突然有事 来不了了')
invitation[2] = '陈六'
print(invitation)
invitation.insert(0,'成龙')
invitation.insert(2,'吴彦祖')
invitation.append('陈冠希')
print(f'邀请{invitation}共进晚餐')
tis = '不好意思 没办法邀请你;'

print(f'一共邀请了{len(invitation)}位嘉宾')
a = invitation[:]
for i in a:

    print(f'{invitation[0]},{tis}')
    invitation.pop(0)
    if not invitation:
        break
print(invitation)

'''
判断列表是否为空
方法一：len()

list1 = []
if len(list1) == 0:
	print("list is empty")

方法二：直接使用if判断
此方法最常用

list2 = []
if not list2:
	print("list is empty")

方法三：使用 空列表进行判断

list3 = []
emptylist = []
if list3 == emptylist:
	print("list is empty")
'''