my_food = ['beans', 'chips', 'fish']
print(my_food) # printing my foods

friends_food = my_food[:] # this makes a copy of my_foods into friends_food but also keeps the lists seperate
print(friends_food)

# just to prove the two lists are not the same adding different items to both of them and then printing
my_food.append('my sauce')
friends_food.append('friends sauce')

print(my_food)
print(friends_food)
