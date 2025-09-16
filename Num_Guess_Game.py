# THIS IS FOR NUMBER GUESSING GAME

import random

top_of_range = input("Type a Number:  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time!")
        quit()

else:
    print("Please enter a number next time!")
    quit()

 
random_num = random.randint(0,top_of_range)

guesses = 0

while True:

    guesses += 1

    user_guess = input("Enter a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print("Please enter a number next time!")
        continue

    if user_guess == random_num:
        print("You Got It!")
        break

    elif user_guess > random_num:
        print(f"You are above the number!")
        
    else:
        print(f"You are below the number!")

print(f"You Guess It in {guesses} Guesse!")