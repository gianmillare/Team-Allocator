import random

print("Welcome to Team Allocator! This version contains up to 3 teams!")


players = ["Craig", "Ben", "Serena", "Amanda",
           "Henry", "Groot", "Gamora", "Widow",
           "Steve", "Tony", "Rocket", "Wasp",
           "Peter", "Bucky", "Pepper", "Alina",
           "Michael", "Dwight", "Pam", "Stanley",
           "Jim", "Janice", "Sandra", "Veronica"]

while True:
    random.shuffle(players)

    team1 = players[:len(players)//3]
    print("\nThe captain for Team 1 is: " + random.choice(team1))
    print("\nThe roster for Team 1 is: ")
    for player in team1:
        print(player)

    team2 = players[len(players)//3:(len(players)//3)*2]
    print("\nThe captain for Team 2 is: " + random.choice(team2))
    print("\nThe roster for Team 2 is: ")
    for player in team2:
        print(player)

    response = input("Would you like to pick teams again? Type 'y' for YES or 'n' for NO: ")

    if response == "n":
        break
