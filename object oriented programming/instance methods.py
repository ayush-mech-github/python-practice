class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def full_name(self):
        return f'full name is {self.first_name} {self.last_name}'

    def is_above_18(self):
        if self.age>18:
            print('adult')
        else :
            print('teen')


p1=Person('ayush','tripathi',21)
p2=Person('ankit','tripathi',21)

print(p1.full_name())
print(p1.is_above_18())
