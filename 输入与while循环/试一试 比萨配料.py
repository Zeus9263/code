# 比萨配料
pizza_list = []
while 1:
    pizza_list_0 = input("请输入比萨的配料,输入quit退出")
    if pizza_list_0 == "quit":
        break
    pizza_list.append(pizza_list_0)
    print(f"我们会在比萨里添加{pizza_list_0}")

print(f"您的披萨里有{pizza_list}请稍等")
