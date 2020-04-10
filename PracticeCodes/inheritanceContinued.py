class SuperA:
    varA = 10
    def funA(self):
        return 11
class SuperB:
    varB = 20
    def funB(self):
        return 21
class Sub(SuperA, SuperB):# multiple inheritance
    pass
obj = Sub()
print(obj.varA, obj.funA())
print(obj.varB, obj.funB())
class Left:
    var = "L"
    varLeft = "LL"
    def fun(self):
        return "Left"
class Right:
    var = "R"
    varRight = "RR"
    def fun(self):
        return "Right"
class Sub(Left, Right): # first itself then bottom to top left to right
    pass
obj = Sub()
print(obj.var, obj.varLeft, obj.varRight, obj.fun())
class One:
    def doit(self):
        print("doit from One")
    def doanything(self):
        self.doit()
class Two(One):
    def doit(self):
        print("doit from Two")
one = One()
two = Two()
one.doanything()
two.doanything() # polymorphism
