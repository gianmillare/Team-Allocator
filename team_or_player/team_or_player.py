import random

print("Welcome to Team or Player Allocator!")

players = ["Craig", "Ben", "Serena", "Amanda",
           "Henry", "Groot", "Gamora", "Widow",
           "Steve", "Tony", "Rocket", "Wasp",
           "Peter", "Bucky", "Pepper", "Alina",
           "Michael", "Dwight", "Pam", "Stanley",
           "Jim", "Janice", "Sandra", "Veronica"]

while True:

    random.shuffle(players)

    user_choice = input("\nIs this for a Team (type 't') or for players (type 'p')? ")

    if user_choice == "t":
        team1 = players[:len(players)//2]
        print("\nThe roster for Team 1 is: ")
        for player in team1:
            print(player)

        team2 = players[(len(players)//2):]
        print("\nThe roster for Team 2 is: ")
        for player in team2:
            print(player)
