# main code for game

import bodyParts as bp
import five as fi
import sixs as si
import seven as se
import random as r
import string

guesses, right_guess = [], []                # list of guesses, right_guess
fails = 0                                    # count of wrong_guess
avail_tries = 7                              # player is a hanged man @ 6 failed guesses
global word                                  # the word selected randomly
letters = string.ascii_uppercase

# function that draws a piece of the hanged man
def hanging(fails):
    if fails == 0:
        print(f'{bp.top} \n {bp.bod_head}{(bp.gallow_head)} \n {bp.bottom}')
    elif fails == 1:
        print(f'{bp.top} \n {bp.bod_head}{bp.neck}{bp.gallow_neck} \n {bp.bottom}')
    elif fails == 2:
        print(f'{bp.top} \n {bp.bod_head}{bp.neck}{bp.left_arm}{bp.gallow_body} \n {bp.bottom}')
    elif fails == 3:
        print(f'{bp.top} \n {bp.bod_head}{bp.neck}{bp.right_arm}{bp.gallow_body} \n {bp.bottom}')
    elif fails == 4:
        print(f'{bp.top} \n {bp.bod_head}{bp.neck}{bp.body}{bp.gallow_bodyx} \n {bp.bottom}')
    elif fails == 5:
        print(f'{bp.top} \n {bp.bod_head}{bp.neck}{bp.body}{bp.left_leg}{bp.gallow} \n {bp.bottom}')
    else:
        print(f'{bp.top} \n {bp.bod_headx}{bp.neck}{bp.body}{bp.right_leg}{bp.gallow} \n {bp.bottom}')
        print(f'YOU HAVE BEEN HANGED ... GAME OVER ...\t THE WORD WAS [{word}]') 


# function to reveal where guessed letter is found in word
def reveal(guess,word,right_guess):
    x = 0
    while x < len(word):
        if guess == word[x]:
            right_guess[x] = guess
        x += 1


# welcome user and ask for category 5,6,7... letter words
cat = int(input('WELCOME TO HANGMAN, PLEASE SELECT A NUMBER BETWEEN 5 AND 7)\t'))
print(f'A {cat} WORD CATEGORY IT IS, BEST OF LUCK BUDDY... HAHAHA!!!')
hanging(fails)


# select a random word from category selected 
if cat == 5:
    word = r.choice(fi.five).upper()
    for x in range(5): right_guess.append('_')
elif cat == 6:
    word = r.choice(si.six).upper()
    for x in range(6): right_guess.append('_')
else:
    word = r.choice(se.seven).upper()
    for x in range(7): right_guess.append('_')


# prompt user to input a letter using a while loop of condition not equal to hangedman final count
while fails < avail_tries:
    print(f'guesses - {guesses}')
    print(f'word - {right_guess}')
    guess = input('Make a guess of a letter in the word above\t').upper()

    # ensure that correct input letters are accepted
    if guess not in letters:
        print('***invalid input***')
        continue

    # ensure repeated inputs are not used to hang player
    if guess in guesses: 
        hanging(fails)
        print(f'the letter {guess} has already been used, please enter another letter')
        continue
    else:
        guesses.append(guess)
        
        # log guess and compare if guess is contained in word
        if guess in word:
            hanging(fails)
            reveal(guess,word,right_guess)
            if '_' not in right_guess: 
                print(f'GOOD JOB PLAYER, YOU WON!!! ... THE WORD IS {right_guess}') 
                break
        else: 
            fails += 1  
            hanging(fails)
            if fails == 6: break
