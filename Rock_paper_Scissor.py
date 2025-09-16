# A ROCK, PAPER, SCISSOR GAME

import random

print(f"\n------------Welcome To The Game!------------")

user_wins = 0
comp_wins = 0

options = ["rock" , "paper" , "scissor"]

while True:

    user_input = input("\nEnter Rock, Paper and Scissor or Enter Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    ran_num = random.randint(0,2)

    # Rock: 0, Paper: 1, Scissor: 2

    comp_pick = options[ran_num]

    print(f"\nComputer Picked : {comp_pick}")


    if user_input == "rock" and comp_pick == "scissor":
        user_wins += 1

    elif user_input == "paper" and comp_pick == "rock":
        user_wins += 1

    elif user_input == "scissor" and comp_pick == "paper":
        user_wins += 1

    else:
        comp_wins += 1

print(f"\nYour win Score is: {user_wins} ")
print("Good Bye!")