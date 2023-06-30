winning_num=56
guess=1#to count number of times of guesses
num=int(input('guess a number between 1 and 100 '))
game_over=False

while not game_over:
    if num==winning_num:
        print(f"you win and you guessed this number in {guess} times")
        game_over=True
    else:
        if num<winning_num:
          print('too low')
          num=int(input('guess again'))
          guess+=1
        else: 
          print('too high')
          num=int(input('guess again'))
          guess+=1

                       #OR

import random
winning_num=random.randint(1,100)#it randomly selects a number between 1 and 100
guess=1#to count number of times of guesses
num=int(input('guess a number between 1 and 100 '))
game_over=False

while not game_over:
    if num==winning_num:
        print(f"you win and you guessed this number in {guess} times")
        game_over=True
    else:
        if num<winning_num:
          print('too low')
        else: 
          print('too high')
    num=int(input('guess again'))
    guess+=1
