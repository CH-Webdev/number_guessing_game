import random
from re import I

random_num = random.randint(1,100)
guess = 0
i = 0
while guess != random_num and guess != "exit":
    guess = input("Guess a number 1 through 100: ")

    if guess == "exit":
        break

    guess = int(guess)
    i += 1

    if guess < random_num:
        print("Too low")
    elif guess > random_num:
        print("Too high")
    else:
        print("You Win!")
        print("Took you only", i, "tries!")
input()
