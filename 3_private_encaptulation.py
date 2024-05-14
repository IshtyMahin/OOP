class A:
    __value = 0
    _val2=-3
    def __init__(self,value) -> None:
        self.__value = value

    def display(self):
        print(self.__value)
        print(self._val2)



obj = A(5)
obj.display()

obj.value = 15
obj.val2 = 10
obj.display()

print(obj.__dict__)


