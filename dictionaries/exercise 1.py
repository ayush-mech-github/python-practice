#define a function that takes a number n
#returns a dictionary containing cubes of numbers from 1 to n

def cube_finder(n):
    cubes={}
    i=1
    while i<=n:
        cubes[i]=i**3
        i+=1
    return d

num=int(input('enter a number'))
print(cube_finder(num))    


def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return d

num=int(input('enter a number '))
print(cube_finder(num)) 
