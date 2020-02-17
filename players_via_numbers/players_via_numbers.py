import random

print("Welcome to Team Allocator! Before proceeding, please assign each member with a number.")

players = []

number_of_players = int(input("How many players will be participating? "))
for i in range(1, number_of_players + 1):
    #print(i, end=', ')
    players.append(i)

random.shuffle(players)

while True:
    team1 = players[:len(players)//2]

    print("\nThe captain for Team 1 is: " + str(random.choice(team1)))
    print("\nThe roster for Team 1 is: ")
    for player in team1:
         print(player)
    
    team2 = players[len(players)//2:]

    print("\nThe captain for Team 2 is: " +str(random.choice(team2)))
    print("\nThe roster for Team 2 is: ")
    for player in team2:
        print(player)

    response = input("Would you like to run the Team Allocator again? Type 'y' for YES or 'n' for NO. ")
    if response == "n":
        break
