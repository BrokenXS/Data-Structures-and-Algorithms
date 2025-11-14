# Nested class is a class defined within another class.
# Benefit is encapsulation and logical grouping of classes.
# keep clean and organized

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_detail(self):
            return (f"{self.name} by {self.position}")
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
        
    def add_employees(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_detail() for employee in self.employees]
company1 = Company("ACB")
company2 = Company("XYZ")

company1.add_employees('Minh', '51')
company1.add_employees('Nghia', '52')

company2.add_employees('dsdsadd', '51')
company2.add_employees('Ngsadsadsadsahia', '52')
print(company1.list_employees())
print(company2.list_employees())

class Nonprofit:
    class Employee:
        pass