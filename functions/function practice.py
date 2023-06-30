#def function_name(parameter1,parameter2,...)
#a function that takes a name as input and returns its last character.
def last_char(name_entered):
    return name_entered[-1]

name=input('enter your name ')
print(last_char(name))

#a function that tells whether a number is odd or even.
def odd_even(num):
    if num%2==0:
        print(f'{num} is even')
    else :
        print(f'{num} is odd')

number=int(input('enter a number '))
print((odd_even(number)))


