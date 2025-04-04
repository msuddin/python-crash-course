user_0 = {
    'first_name': 'John',
    'last_name': 'Smith',
    'email': 'test@test.com',
}

for key, value in user_0.items():
    print(key)
    print(value + "\n")

# Only print the keys
for key in user_0.keys():
    print(key)