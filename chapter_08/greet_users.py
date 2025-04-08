def greet_users(users):
    for user in users:
        print(f'Hello {user.title()}!')

users = ['jessy', 'sam', 'kurt']
greet_users(users)