import random


u_win = 0
c_win = 0

option = ["rock", "paper", "scissor"]

while True:

    u_input = input("\nType Rock, Paper, Scissor or Q to quit: ").lower()

    if u_input == "q":
        break

    if u_input not in option:
        continue

    ran_num = random.randint(0,2)

    c_pick = option[ran_num]
    print(f"\nComputer picked {c_pick}")

    if u_input == "rock" and c_pick == "scissor":
        u_win += 1

    elif u_input == "paper" and c_pick == "rock":
        u_win += 1

    elif u_input == "scissor" and c_pick == "paper":
        u_win += 1

    else:
        c_win += 1

print(f"\nYou wins {c_win} times!")
