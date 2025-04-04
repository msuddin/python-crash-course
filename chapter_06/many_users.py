many_users = {
    'jimmy': {
        'fname': 'jimmy',
        'sname': 'jones',
        'age': 10,
    },
    'karl': {
        'fname': 'karl',
        'sname': 'hands',
        'age': 15,
    }
}

for user, info in many_users.items():
    print(user, info)

# Print the age only
for user, info in many_users.items():
    print(user, info['age'])