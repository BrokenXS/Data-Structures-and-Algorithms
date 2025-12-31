#static method
class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_info(self):
            return f"Employee: {self.name}, Position: {self.position}"
        
        @staticmethod
        def is_valid_position(position: str) -> bool:
            valid_positions = ['Manager', 'Developer', 'Designer', 'Intern']
            return position in valid_positions

print(Employee.is_valid_position("ABC"))    

#Class method

class Student:
    count = 0
    total_gpa = 0.0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    def get_info(self):
        return f"Student: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def get_student_count(cls):
        return f"Total students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        return cls.total_gpa / cls.count
    
student1 = Student("Minh", 3.5)
student2 = Student("Nghia", 3.8)
student3 = Student("An", 3.9)

print(Student.get_student_count())
print(Student.get_average_gpa())