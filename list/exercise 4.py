#filter odd even
#define a function
#input
#list --->[1,2,3,4,5,6,7,8,9]
#output ----> [[1,3,5,7,9],[2,4,6,8]]

def even_odd(l):
    even=[]
    odd=[]
    matrix=[]
    for element in l:
        if element %2==0:
            even.append(element)
        else :
            odd.append(element)
    matrix=[even,odd]
    return matrix

l=list(range(1,11))
print(even_odd(l))
