
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name)
        print(self.age)
     
class Academic:
    def __init__(self,cgpa):
        self.cgpa = cgpa
    
    def display(self):
        print(self.cgpa)   

class Student(Person,Academic):
    def __init__(self, name, age, rollno,cgpa):
        Person.__init__(self,name, age)
        Academic.__init__(self,cgpa)
        self.rollno = rollno
        
    def display(self):
        Person.display(self)
        print(self.rollno)
        Academic.display(self)
        
        

obj = Student("Ishtiaq", 20, 101,3.84)

obj.display()

        
        