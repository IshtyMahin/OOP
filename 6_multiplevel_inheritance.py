
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name)
        print(self.age)
        

class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno
        
    def display(self):
        Person.display(self)
        print(self.rollno)
        
    
class UniversityStudent(Student):
    def __init__(self, name, age, rollno, major):
        super().__init__(name,age,rollno)
        self.major = major
        
    def display(self):
        Student.display(self)
        print(self.major)
        

obj = UniversityStudent("Ishtiaq", 20, 101, "CSE")

obj.display()