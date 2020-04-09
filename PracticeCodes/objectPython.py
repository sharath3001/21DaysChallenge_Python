class Stack:    # defining the Stack class
    def __init__(self):    # defining the constructor function
        print("Hi!")
stackObject = Stack()    # instantiating the object
class Stack:
    def __init__(self):
        self.stackList = [] # self.__stackList = [] to declare stackList private
stackObject = Stack()
print(len(stackObject.stackList))
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val): # one parameter is always compulsory
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
stackObject = Stack()
stackObject.push(3)
stackObject.push(2)
stackObject.push(1)
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
stackObject = AddingStack()
for i in range(5):
    stackObject.push(i)
print(stackObject.getSum())
for i in range(5):
    print(stackObject.pop())
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def setSecond(self, val):
        self.second = val
exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject2.setSecond(3)
exampleObject3 = ExampleClass(4)
exampleObject3.third = 5 # instance variables
print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val
    def setSecond(self, val = 2):
        self.__second = val
exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject2.setSecond(3)
exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5
print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)
print(exampleObject1._ExampleClass__first) # using this we can access private properties
class ExampleClass:
    counter = 0 # class variable
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)
print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val
print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)
print(ExampleClass.__dict__)
print(exampleObject.__dict__)
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
exampleObject = ExampleClass()
print(hasattr(exampleObject, 'b')) # to check existence of particular variable
print(hasattr(exampleObject, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
