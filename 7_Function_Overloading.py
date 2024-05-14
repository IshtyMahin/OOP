

def sum(a, b):
    return a + b

def sum(a, b, c):
    return a + b + c 

# print(sum(1, 3)) #  error dibe
print(sum(1, 2,3))

# function overloading evabe kora jai na , evabe korle last er function ta kaj kore , ager ta use korle error dibe


# jodi amar overloading kora lage tahole nicher moto kore default value=0 use kore kora jabe
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


cal = Calculator()

print(cal.add(2))       
print(cal.add(2, 3))    
print(cal.add(2, 3, 4)) 
print(cal.add(2.4,4.5))