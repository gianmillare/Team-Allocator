import random

print("Welcome to Team Allocator!")

players = ["Geoff", "David", "Alayah", "Natasha",
           "Craig", "Ben", "Serena", "Amanda",
           "Henry", "Groot", "Gamora", "Widow",
           "Steve", "Tony", "Rocket", "Wasp",
           "Peter", "Bucky", "Pepper", "Alina",
           "Michael", "Dwight", "Pam", "Stanley",
           "Jim", "Janice", "Sandra", "Veronica"]


while True:

    random.shuffle(players)

    team1 = players[:len(players)//2]
    print("The captain for Team 1 is: " + random.choice(team1))
    print("Team 1: ")

    for player in team1:
        print(player)


    print("-------------------------------------------------------")


    team2 = players[:len(players)//2]
    print("The captain for Team 2 is: " + random.choice(team2))
    print("Team 2: ")

    for player in team2:
        print(player)
