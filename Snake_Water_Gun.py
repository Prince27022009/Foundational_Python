options = ["snake", "water", "gun"]

meanings = {
"snake" : "snake",
"water" : "water",
"gun" : "gun",
"exit" : "exit",
"s" : "snake",
"w" : "water",
"g" : "gun",
"q" : "exit"
}
#Meanings of input terms for program.

mechanics = {
"snake" : "water", # snake drinks water.
"water" : "gun", # gun sinks under water.
"gun" : "snake", # gun shoots snake.
} 
#Mechanics on what wins over what

meanings2 = {
"yes" : "yes",
"y" : "yes"
}

import sys
a1 = input("Do you wanna continue? Type y/yes to play. Type anything else to exit").lower()
a = meanings2.get(a1)
if a != "yes":
    print("Thanks!")
    sys.exit()

import random
print("\nChoose: \ns/snake for snake.\nw/water for water.\n g/gun for gun.")
computer = random.choice(options)#Random choice of computer.

non_player = input("\nEnter your choice").lower()
player = meanings.get(non_player)

if player is None:
    print("Invalid input. please put from the ones mentioned below") 
#In case someone inputs wrong, program doesn't show an error.

print("\nYou choose: ", player)
print("Computer chose: ", computer)

def game():
    if player == computer:
        print("It's a tie")
    elif mechanics[player] == computer:
        print("You won")
    else:
        print("You lose")
game()


while True:
    computer = random.choice(options) #Random choice.

    print("\nChoose: \ns/snake for snake.\nw/water for water.\ng/gun for gun.\nq/exit to quit")

    non_player = input("Enter your choice").lower()
    player = meanings.get(non_player)#converts everything to snake,                                                                    water, gun.
    if player is None:
        print("Invalid input. please put from the ones mentioned below")
        continue
        #In case someone inputs wrong, program doesn't show an error  
    
    if player == "exit":
        print("Thanks for playing")
        break               
       #To exit the game.

    print("You choose: ", player)
    print("Computer chose: ", computer)
    
    game()   
