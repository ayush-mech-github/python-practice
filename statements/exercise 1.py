#EXERCISE , NUMBER GUESSING GAME
#make a variable, like winning_number and assign any number to it.
#ask user to guess a number.
#if user guessed correctly the  print 'YOU WIN !!!'
#if user didn't guess correctly then :
    #if user guessed lower than actual number then print 'too low'
    #if user guessed lower than actual number then print 'too high'

winning_number=5
number=int(input('enter a number between 1 and 10 '))
if number==winning_number:
    print('YOU WIN !!!')
else:
    if number<winning_number:
        print('too low')
    else:
        print('too high')
