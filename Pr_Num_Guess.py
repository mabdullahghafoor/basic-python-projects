import random

num_range = input(f"\nEnter a Number For a Range You Want To Guess: ")

if num_range.isdigit():
    num_range = int(num_range)

    if num_range <= 0:
        print(f"\nlease enter a number greator than zero next time!")
        quit()

else:
    print(f"\nPlease Enter a digit next time!")
    quit()

ran_num = random.randint(0,num_range)
guess = 0


while True:

    num = input("\nEnter a number for a guess: ")

    guess += 1

    if num.isdigit():
        num = int(num)

        if num <= 0:
            print(f"\nlease enter a number greator than zero next time!")
            quit()

    else:
        print(f"\nPlease Enter a digit next time!")
        quit()

    if num == ran_num:
        break

    elif num < ran_num:
        print(f"\nYou are below!")

    else:
        print(f"\nYou are above!")


print(f"\nSuccess!")
print(f"\nYou got in {guess} guesses!")