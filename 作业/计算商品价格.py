print("************************************")
print("单号:10249781290571023")
print("2021-3-17 17:09:09")
print("************************************")
price_total = 0
name = int(input("商品名:"))
count = int(input("数量:"))
price = int(input("支付金额:"))
total = count * price
price_total = price_total + total
print("************************************")
print('名称', '数量', '单价', '金额', sep='\t')
print(name, count, price, total, sep='\t\t')
print('牛肉干')
count = 3
price = 35
total = count * price
price_total = price_total + total
print(name, count, price, total, sep='\t\t')
print('卫生纸')
count = 2
price = 6
total = count * price
price_total = price_total + total
print(name, count, price, total, sep='\t\t')
print('篮球')
count = 1
price = 161
total = count * price
price_total = price_total + total
print(name, count, price, total, sep='\t\t')
print("************************************")
print("收银合计:\t\t\t\t\t", price_total)
print(f"您共消费:{price_total}元。", )
print("************************************")
print("感谢你的惠顾，欢迎下次再来！\n收银员：001")