players = ['Charles','Martina','Michael,','Florence','Eli']
print(players[0])
print(players[1]) 
print(players[2])
print(players[3])
print(players[4])
some_players = players[0:3] #starting at index 0 and ending at index 3
print(some_players)
print(players[1:4])
print(players[:4]) #skip the first index it's like starting at index 0
print(players[2:]) #skip the last index it's like ending at the last index
print(players[-3:]) #print the last three players
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())