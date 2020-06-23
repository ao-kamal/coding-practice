import random
import sys

fin = open('words.txt')

easy_level = []
medium_level = []
hard_level = []

hang_word = ''


def level_list():
    for line in fin:
        word = line.strip()
        if len(word) == 3:
            easy_level.append(word)
        elif len(word) == 4:
            easy_level.append(word)
        elif len(word) == 5:
            medium_level.append(word)
        elif len(word) == 6:
            hard_level.append(word)
        elif len(word) == 7:
            hard_level.append(word)


def level_select():
    print('----------------------------------------------------------')
    print('Guess the word game.')
    print('(Idiot proof!)')
    print('\n')
    level = input('Pick a Difficulty (Easy, Medium, Hard):\n')
    global hang_word
    level_list()
    if level == 'Easy':
        hang_word = random.choice(list(easy_level))
    elif level == 'Medium':
        hang_word = random.choice(list(medium_level))
    elif level == 'Hard':
        hang_word = random.choice(list(hard_level))
    else:
        print('Pick a level, you retard!')
        level_select()


def end_prompt():
    print("To play again, hit Enter. To exit, type 'Fuck Off'")
    response = input()
    if response == '':
        level_select()
        empty_word = len(hang_word) * ['_']
        validate_guess()
    elif response == 'Fuck Off':
        print('Bye Bitch!')
        sys.exit()
    else:
        print('You typed ' + "'" + response + "' , you retard!")
        end_prompt()


def validate_guess():
    num_guess = (len(hang_word) + 3)
    while num_guess != 0:
        guess = (input("I'm thinking of a word. What do you think it is?\n(PS. You have to guess letter by letter. You have " +
                       str(num_guess) + ' guesses left.)\n')).lower()
        if len(guess) < 1:
            print('One guess at a time, motherfucker!')
            print('\n')
            continue
        elif len(guess) > 1:
            print('One guess at a time, motherfucker!')
            print('\n')
            continue
        elif guess.isalpha() == False:
            print('Enter a letter, not a number.')
            print('\n')
            continue
        else:
            global empty_word
            index = 0
            if guess in hang_word:
                while index < len(hang_word):
                    if hang_word[index] == guess:
                        empty_word[index] = guess
                        if '_' not in empty_word:
                            print('You guessed right!')
                            end_prompt()
                            break
                    index += 1
            elif guess not in hang_word:
                print('The letter ' + "'" + guess +
                      "'" + " isn't in the word.")

        num_guess -= 1
        print(''.join(empty_word))

    if '_' in empty_word:
        print('Shame on you!\nThe word is ' + "'" +
              (''.join(hang_word)) + "'" + '.')

    end_prompt()


level_select()

empty_word = len(hang_word) * ['_']

validate_guess()

# TODO: find a more suitable wordlist
# TODO: fill out random letters before start
# TODO: you've already filled that in prompt
# TODO: you guessed correctly
