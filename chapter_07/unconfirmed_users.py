# Moving items from one list to another

# Get a list of unconfirmed users
unconfirmed_users = ['ray', 'aya', 'zay', 'demon']
confirmed_users = []

print(f"Print list of unconfirmed users: {unconfirmed_users}")
print(f"Print list of confirmed users: {confirmed_users}")

# While loop to take items from one list and insert into another
# Also checking to ignore users
while unconfirmed_users:
    if 'demon' in unconfirmed_users:
        print('Found demon in unconfirmed users, removing the user')
        unconfirmed_users.remove('demon')
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print(f"Confirm user: {current_user}")

print(f"Print list of unconfirmed users: {unconfirmed_users}")
print(f"Print list of confirmed users: {confirmed_users}")