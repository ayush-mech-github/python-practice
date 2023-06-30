class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_str(cls, emp_str):
        name, age, salary = emp_str.split('-')
        return cls(name, age, salary)


ayush = Employee.from_str('ayush-22-85000')
print(ayush.name)
print(ayush.age)
print(ayush.salary)
