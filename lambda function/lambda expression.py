#lambda expression (anonymous function)

def add(a,b):
    return a+b
print(add(3,5))

add2=lambda a,b:a+b
print(add2(4,6))

multiply=lambda a,b:a*b
print(multiply(2,3))

#proof that lambda is an anonymous function
print(add)
print(add2)
print(multiply)
