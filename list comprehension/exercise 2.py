#define a function that takes a list as input and
#returns a list with int and float values in the original list

mixed=['ayush',{1:1,2:[1,2]},(1,2,3),{4,5,6},7,8,9,10.0,10.1]

numbers=[str(i) for i in mixed if (type(i)==int or type(i)==float)]
print(numbers)

def num(l):
    num1=[]
    for element in l:
        if type(element)==int or type(element)==float:
            num1.append(str(element))
    return num1       

print(num(mixed))
