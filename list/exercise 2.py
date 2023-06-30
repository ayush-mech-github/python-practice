#define a function that takes list as a argument and
#returns reversed list

def reverse_list(l):
    l.reverse()
    return l

l=list(range(1,11))
print(reverse_list(l))


                      #OR


def reverse_list(l):
    return l[::-1]

l=list(range(1,11))
print(reverse_list(l))


                    #using pop() method
def reverse_list(l):
    reversed_list=[]
    for element in range(len(l)):
        popped_item=l.pop()
        reversed_list.append(popped_item)
    return reversed_list

l=list(range(1,11))
print(reverse_list(l))
