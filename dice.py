import random


def rand():
    print('The die roll returned ' + str(random.randint(1, 6)))
    prompt = input('Would you like to print again?\n')
    if prompt == 'Yes':
        rand()
    elif prompt == 'No':
        print('Bye!')
    else:
        print("That's not a valid answer")


rand()
