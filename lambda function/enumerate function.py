#we use enumerate function with for loop to track the poition of our
#element in iteration

#without using enumerate function
names=['ayush','amit','utkarsh']
position=0
for element in names:
    print(f'{element} is present at {position}')
    position+=1


#using enumerate function
names=['ayush','amit','utkarsh']
for position,element in enumerate(names):
    print(f'{element} is present at {position}')


#define a function that takes two arguments
# 1) list containing string
# 2) string that you want to find in your list
# and this function will return the index of string in your list
# and if string is not present, return -1

def find(s,find_s):
    for position,string in enumerate(s):
        if string==find_s:
            s.append(position)
        else :
            s.append(-1)
    return s

s=['ayush','amit','utkarsh']
find_s=input('enter the string in s whose position you want to know')
print(find(s,find_s))

