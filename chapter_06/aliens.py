# A list full of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'green', 'points': 5}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


bad_aliens = []

for bad_alien in range(10):
    new_alien = {'color': 'green', 'points': 5}
    bad_aliens.append(new_alien)

print(bad_aliens[:5])