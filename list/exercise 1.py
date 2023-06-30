#define a function that takes a list as input
#and returns list containing square of each element

def list_square(l):
    square_list=[]
    for element in l:
        square_list.append(element**2)
    return square_list

original_list=list(range(3,11))
print(list_square(original_list))



