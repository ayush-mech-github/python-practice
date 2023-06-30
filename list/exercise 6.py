#function that takes a list as input and tells
#how many sublists that list contains

def sublists(l):
    count=0
    for element in l:
        if type(element)==list:
            count+=1
    return count

l=[1,2,[3,4],[5,6],['ayush']]
print(sublists(l))
