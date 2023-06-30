#define a function that takes list of words as argument and
#returns list with reverse of every element in that list

#example
#['abc','xyz'] --> ['cba','zyx']

def reverse(l):
    new_list=[]
    for element in l:
        new_list.append(element[::-1])
    return new_list

l=['ayush','gagan','amit']
print(reverse(l))
