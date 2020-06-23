import random


def guess_num():
    num = random.randint(1, 100)

    while True:
        guess = int(input("Guess the number.\nHint: It's between 1 and 100\n"))
        if guess > num:
            print('Too high! Try again.')
        elif guess < num:
            print('Too low! Try again.')
        elif guess == num:
            print('You guessed right!')
            break


guess_num()
