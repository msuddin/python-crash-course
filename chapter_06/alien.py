alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # print the alien
print(alien_0['color']) # print the value of color
print(alien_0['points']) # print the value of points

new_points = alien_0['points']
print(f"You just earned {new_points} points.")

# Adding key value pairs to dictionaries
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'fast'
print(alien_0)

# We can increase the speed of the alien based on some setting
x_increment = 0
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

# Update the position of the alien
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)

alien_1 = {} # Staring with an empty alien
alien_1['x_position'] = 100
alien_1['y_position'] = 25
print(alien_1)

# You can also remove key value pairs
alien_0['god_mode'] = True
print(alien_0)
del alien_0['god_mode']
print(alien_0)