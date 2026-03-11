class Employee:
    def __init__(self, id: int, salary: int):
        self.id = id
        self.salary = salary
    def get_info(self):
        return f"Employee ID: {self.id}, Salary: {self.salary}"

class SalesEmployee(Employee):
    def __init__(self, id: int, salary: int, sales: int = 0):
        super().__init__(id, salary)
        self.sales = sales

    def get_info(self) -> str:
        return f"EmployeeID:{self.id} Salary:{self.salary} Sales:{self.sales}"

e1 = Employee(104, 70000)
print(e1.get_info())

s1 = SalesEmployee(102, 60000, 150)
print(s1.get_info())

s2 = SalesEmployee(103, 55000, 5)
print(s2.get_info())
