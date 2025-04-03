players = ['jimmy', 'timmy', 'suzzie', 'peter']
print(players) # print all players
print(players[0:3]) # print from index position 0 to 3 only
print(players[1:3]) # print from index position 1 to 3 only
print(players[:3]) # print up to index position 3
print(players[2:]) # print from index position 2

for player in players[2:]: # only get players after index position 2
    print(player.title())