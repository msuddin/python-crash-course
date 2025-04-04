prompt = '\nTell me something and I will repeat it.'
prompt += '\nBut if you type quit then I will stop. '

message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

    if message == 'quit':
        print('Thanks for playing!')