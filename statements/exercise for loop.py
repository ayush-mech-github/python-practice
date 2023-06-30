#sum from 1 to 10.
total=0
for i in range(1,11):
    total=total+i
print(f'sum is {total}')

#ask user for a number and print sum of digits of the number.
n=input('enter a number')
total=0
for i in range(0,len(n)):
    total+=int(n[i])
print(f'sum of digits is {total}')

                         #OR
n=input('enter a number')
total=0
for i in n:
    total+=int(i)
print(f'sum of digits is {total}')



#ask user for its name and count each character.
name=input('enter your name')
var_string=''
for i in range(len(name)):
    if name[i] not in var_string:
        var_string+=name[i]
        print(f'{name[i]} comes {name.count(name[i])} times')
        
