import random

print("Welcome to Team Allocator! Before proceeding, please assign each member with a number.")

players = []

number_of_players = int(input("How many players will be participating? "))
for i in range(1, number_of_players + 1):
    #print(i, end=', ')
    players.append(i)

random.shuffle(players)

team1 = players[:len(players)//2]

print("\nThe captain for Team 1 is: " + str(random.choice(team1)))
print("\nThe roster for Team 1 is: ")
for player in team1:
     print(player)
    
