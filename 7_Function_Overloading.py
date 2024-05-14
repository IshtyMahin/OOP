# python does not support method overloading. We may define many methods of the same name and different arguments, but we can only use the latest defined method. 


def sum(a, b):
    return a + b

def sum(a, b, c):
    return a + b + c 

# print(sum(1, 3)) # give error
print(sum(1, 2,3))

# We achieve this by using default parameter values in the function

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


cal = Calculator()

print(cal.add(2))       
print(cal.add(2, 3))    
print(cal.add(2, 3, 4)) 
print(cal.add(2.4,4.5))