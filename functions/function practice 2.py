# define a function that takes two numbers as input and returns greater of two numbers.
def greater_number(num1, num2):
    if num1 > num2:
        return num1
    return num2


number1, number2 = input('enter two numbers ').split()
# number1=int(number1)
# number2=int(number2)
print(f'{greater_number(number1,number2)} is greater number')

# define a function that takes three numbers as input and returns greatest of three numbers.


def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


x, y, z = input('enter any three comma seperated numbers').split(',')
x = int(x)
y = int(y)
z = int(z)
print(f'{greatest(x,y,z)} is the greatest number')
