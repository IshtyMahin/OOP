
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
        super().display()
        print(self.rollno)
        

obj = Student("Ishtiaq", 20, 101)

obj.display()

        