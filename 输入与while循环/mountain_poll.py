# mountain_poll
responses = {}

# 设置一个标志 指出调查是否继续
poliling_active = True
while poliling_active:
    # 提示输入被采访者的名字和回答
    name = input("请输入你的名字")
    response = input("你喜欢爬哪座山")
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("是否还有人要参与调查(yes/no)")
    if repeat == 'no':
        poliling_active = False
print("\n--- Poll Results---")
print(responses)
for name, response in responses.items():
    print(f"{name} 喜欢爬 {response}.")