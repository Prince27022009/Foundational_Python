import random

# Player stats
player = {
    "health": 50,
    "inventory": [],
    "current_room": "Entrance"
}

# Rooms and items
rooms = {
    "Entrance": {"description": "You are at the entrance of a dark cave.", "paths": ["Left Room", "Right Room"], "item": None},
    "Left Room": {"description": "A small room with a shiny key on the floor.", "paths": ["Entrance"], "item": "Key"},
    "Right Room": {"description": "A quiet room with a locked chest. A Boss guards it!", "paths": ["Entrance"], "item": "Treasure"}
}

# Boss stats
boss = {"name": "Cave Guardian", "health": 40}

# Show player status
def show_status():
    print(f"\nYou are at {player['current_room']}")
    print(f"Health: {player['health']}")
    print(f"Inventory: {player['inventory']}")

# Move player
def move_player():
    current = player["current_room"]
    print(f"\n{rooms[current]['description']}")
    print("Paths available:", ", ".join(rooms[current]["paths"]))
    choice = input("Where do you want to go? ").title()
    if choice in rooms[current]["paths"]:
        player["current_room"] = choice
        enter_room()
    else:
        print("This is a Dead End!")

# Room events
def enter_room():
    room = player["current_room"]
    item = rooms[room]["item"]
    
    if room == "Left Room" and item and "Key" not in player["inventory"]:
        print(f"You found a {item}!")
        player["inventory"].append(item)
        rooms[room]["item"] = None

    elif room == "Right Room":
        # Trap if player doesn't have Key
        if "Key" not in player["inventory"]:
            trap_damage = 10
            player["health"] -= trap_damage
            print("\nThe gate is locked. You need a Key to open.")
            print("You forcefully tried to open the gate. Trap activated!")
            print(f"Poison arrow hit you. Current health: {player['health']}")
            return
        fight_boss()

# Boss fight
def fight_boss():
    print(f"\nA {boss['name']} attacks to protect the Treasure!")
    while boss["health"] > 0 and player["health"] > 0:
        attack = random.randint(5, 15)
        boss["health"] -= attack
        print(f"You hit {boss['name']} for {attack} damage.")
        if boss["health"] <= 0:
            print("Boss defeated! You open the chest and find the Treasure! You win!")
            exit()
        
        boss_attack = random.randint(5, 12)
        player["health"] -= boss_attack
        print(f"{boss['name']} hits you for {boss_attack} damage. Your health: {player['health']}")
        if player["health"] <= 0:
            print("You were defeated by the Boss. Game Over.")
            exit()

# Main game loop
def game():
    print("Welcome to the Mini Adventure Game!")
    print("Commands: move, status, quit")
    
    while True:
        command = input("\nGive your command:  ").lower()
        if command == "move":
            move_player()
        elif command == "status":
            show_status()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    game()
