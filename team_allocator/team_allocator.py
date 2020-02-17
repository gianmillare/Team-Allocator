import random

print("Welcome to Team Allocator!")

players = ["Geoff", "David", "Alayah", "Natasha",
           "Craig", "Ben", "Serena", "Amanda",
           "Henry", "Groot", "Gamora", "Widow",
           "Steve", "Tony", "Rocket", "Wasp",
           "Peter", "Bucky", "Pepper", "Alina",
           "Michael", "Dwight", "Pam", "Stanley",
           "Jim", "Janice", "Sandra", "Veronica"]


random.shuffle(players)

team1 = players[:len(players)//2]

print("The captain for Team 1 is: " + random.choice(team1))

print("Team 1: ")

for player in team1:
    print(player)
