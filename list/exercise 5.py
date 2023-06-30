#define a function that takes two lists as input and
#returns common elements of both lists

#example
#input ---->  [1,2,5,8],[1,2,3,4]
#output ----->  [1,2]

def common(l1,l2):
    l3=[]
    for element in l1:
        if element in l2:
            l3.append(element)
    return l3

l1=[1,2,3,5,6,9]
l2=[1,2,3,4,7]
print(common(l1,l2))

