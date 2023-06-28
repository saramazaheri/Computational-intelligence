import random

# List of players
players = []

# Function to add players
def add_player(name):
    players.append(name)

# Function to remove players
def remove_player(name):
    players.remove(name)

# Function to randomly select a player as the winner
def select_winner():
    if len(players) > 0:
        winner = random.choice(players)
        print(f"The winner is {winner}!")
    else:
        print("No players remaining.")

# Main game loop
while True:
    print("Squid Game")
    print("1. Add Player")
    print("2. Remove Player")
    print("3. Select Winner")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter player name: ")
        add_player(name)
        print(f"Player {name} added.")

    elif choice == "2":
        name = input("Enter player name: ")
        if name in players:
            remove_player(name)
            print(f"Player {name} removed.")
        else:
            print(f"Player {name} not found.")

    elif choice == "3":
        select_winner()

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")

print("Thanks for playing Squid Game!")
