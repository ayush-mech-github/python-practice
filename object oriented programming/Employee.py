class Employee:
    increment = 1.5

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        self.salary = self.salary*Employee.increment


# objects
ayush = Employee('ayush', 50000)
ankit = Employee('ankit', 10000)

print(ayush.salary)
# print(Employee.__dict__)  # to get all the variables of Employee
ayush.increase_salary()
print(ayush.salary)
