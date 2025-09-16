# THIS PROJECT IS DESIGN FOR A COMPUTER QUIZ GAME

print(f"\nWelcome To My Computer Quiz Game! :)") 

playing = input(f"\nDo You Want To Play? ")

if playing.lower() != "yes":
    quit()

print(f"\nOkay! Let's Play :) ")

score = 0

answer = input("\nwhat does CPU stands for? ")
if answer.lower() == "central processing unit":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

answer = input("\nwhat does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

answer = input("\nwhat does RAM stands for? ")
if answer.lower() == "random access memory":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

answer = input("\nwhat does PSU stands for? ")
if answer.lower() == "power supply unit":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

print(f"\nYou got {score} questions correct! ")
print(f"\nYou got {((score/ 4)*100)}")
