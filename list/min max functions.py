numbers=[1,2,3,4,5,6,7,8,9]
print(min(numbers))
print(max(numbers))

#define a function that takes a list of numbers as input and
#returns gretest difference of numbers in the list

def greatest_difference(l):
    difference=max(l)-min(l)
    return difference

l=list(range(1,11))
print(greatest_difference(l))
