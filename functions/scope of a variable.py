x=5#global variable

def func():
    x=7#local variable
    return x

print(func())#output - 7
print(x)#output - 5




x=5#global variable

def func():
    global x#working on global variable
    x=7
    return x

print(func())#output - 7
print(x)#output - 7
