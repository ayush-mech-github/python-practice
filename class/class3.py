class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print('hello my name is ' +self.name)

p1=Person('Ayush',21)
p1.myfunc()
