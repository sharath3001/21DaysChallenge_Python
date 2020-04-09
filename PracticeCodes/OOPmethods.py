class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
obj = Classy()
obj.var = 3
obj.method()
class Classy:
    def visible(self):
        print("visible")
    def __hidden(self): # partially hidden
        print("hidden")
obj = Classy()
obj.visible()
try:
    obj.__hidden()
except:
    print("failed")
obj._Classy__hidden()
class Classy:
    pass
print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)
class Classy:
    pass
print(Classy.__module__)
obj = Classy()
print(obj.__module__)
class SuperOne:
    pass
class SuperTwo:
    pass
class Sub(SuperOne, SuperTwo):
    pass
def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')
printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
class MyClass:
    pass
obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5
def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)
print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
