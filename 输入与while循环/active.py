# active
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"

active = True  # 标志 flag
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        # break
    else:
        print(message)