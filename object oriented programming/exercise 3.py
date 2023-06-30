#WAP that counts number of instances in a class
#use the fact that every time an instance is created,__init__ method is called
class Person:
    count=0
    def __init__(self,name,age):
        Person.count+=1
        self.name=name
        self.age=age

p1=Person('ayush',21)
p2=Person('ankit',21)
p3=Person('himanshu',20)
print(f'number of instances is {Person.count}')

    
