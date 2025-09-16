print(f"\n----------Welcome To The Practice Quiz Game!----------")

choice = input(f"\nDo you Want To Play?")

if choice.lower() != "yes":
    quit()

print(f"\nYou Have To Answer The Following questions!")
score = 0

answer = input(f"\nWhat does CPU stands for?")
if answer.lower() == "central processing unit":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

answer = input(f"\nWhat does GPU stands for?")
if answer.lower() == "graphic processing unit":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

answer = input(f"\nWhat does RAM stands for?")
if answer.lower() == "random access memory":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

answer = input(f"\nWhat does PSU stands for?")
if answer.lower() == "power supply unit":
    print(f"\nCorrect!")
    score += 1
else:
    print(f"\nIncorrect!")

print(f"\nQuiz Completed!")
print(f"\nYou got {score} correct  out of 4")
print(f"\nYour success percentage is {((score)/4)*100} %")