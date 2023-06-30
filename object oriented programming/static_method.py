class Employee:

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    @staticmethod
    def is_open(day):
        if day == 'sunday':
            return False
        else:
            return True


e1 = Employee('deepak', 22, 40000)
print(e1.name)

print(Employee.is_open('monday'))


