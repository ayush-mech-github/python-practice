#input user name and print reverse of it
name=input('enter your name')
print(f'reverse of your name is {name[::-1]}')

#take two comma seperated input from user
#1. user's name 2. a single character

#output - 2 print lines
#1. user's name length
#2. count the character that user inputs (case insensitive)

name,character=input('enter space seperated name and character').split()
print(f'name length is {len(name)}')
print(f'number of times character comes in the name is {name.lower().count(character.lower())}')
