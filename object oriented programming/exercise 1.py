# create a laptop class with attributes like name,processor name,price
# create two objects/instance of your laptop class

class Laptop:
    def __init__(self, name, processor, price):
        self.name = name
        self.processor = processor
        self.price = price


l1 = Laptop('asus', 'ryzen', 42000)
print(l1.name)
print(l1.processor)
print(l1.price)
