#generate list with range function
numbers=list(range(1,11))
print(numbers)

#pop method
numbers=list(range(1,11))
poped_item=numbers.pop()
print(numbers)
print(poped_item)

#index method
numbers=list(range(1,11))
print(numbers.index(5))
numbers1=[1,2,3,4,5,6,7,8,1]
print(numbers1.index(1,1))#starts searching from 1st index

#function that returns negative of a list
numbers=list(range(1,11))
def negative_list(l):
    l1=[]
    for i in l:
        l1.append(-i)
    return l1

print(negative_list(numbers))

