prompt = '\nTell me the name of the city you wish to search.'
prompt += '\nBut if you type quit then I will stop. '

flag = True
while flag:
    message = input(prompt)
    if message == 'quite':
        print('You may have mis-spelt quite')
        continue
    if message == 'quit':
        flag = False
        print('\nThank you for playing!')
        break
    print(f"Nothing found for {message}")

print('End of search')