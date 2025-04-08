# this returns the user as a dictionary
def get_user(first_name, last_name):
    return {'first_name': first_name, 'last_name': last_name}

john = get_user('John', 'Smith')
print(john)

loop = 0
while loop < 5:
    person = get_user(f'f_name_{loop}', f'l_name_{loop}')
    print(person)
    loop = loop + 1