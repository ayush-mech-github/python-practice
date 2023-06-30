# it is just  way/style of writing code
# very helpful in solving real world problems
# init method is used as constructor
# any function defined in a class is called method
# self represents our object
# __init__ method is called every time we create an instance/object

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# objects
p1 = Person('ayush', 'tripathi', 21)
p2 = Person('ankit', 'tripathi', 21)

print(p1.first_name)
