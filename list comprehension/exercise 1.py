#define a function that takes a list of strings as input and
#returns a list containing reverse of every string

def reverse(l1):
    l2=[]
    for string in l1:
        l2.append(string[::-1])
    return l2
l1=['ayush','gagan']
print(reverse(l1))

l3=['ayush','gagan']
l4=[name[::-1] for name in l3]
print(l4)


        
