class Laptop:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def percentage_discount(self, percentage_off):
        new_price = self.price-(self.price*percentage_off)/100
        return new_price


l1 = Laptop('samsung', 'm1', 20000)
print(l1.name, l1.model, l1.price)
print(l1.percentage_discount(40))
