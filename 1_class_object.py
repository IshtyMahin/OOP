
class Person: 
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f'{self.name} {self.age}'
        
    def display(self):
        print(f'Hello {self.name}')
        
A=Person("Mahin",20)
A.display()

# modify obj property
A.age=22
# delete obj property 
del A.age 

print(A)

# delete obj 
del A
    