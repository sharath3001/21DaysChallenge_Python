class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self): # in built method returns class and address
        return self.name + ' in ' + self.galaxy
sun = Star("Sun", "Milky Way")
print(sun)
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()
for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
class SampleClass:
    def __init__(self, val):
        self.val = val
ob1 = SampleClass(0)
ob2 = SampleClass(2)
ob3 = ob1
ob3.val += 1
print(ob1 is ob2) # is operator checks whether both point to the same memory
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)
str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)
obj = Sub("Andy")
print(obj)
print(str1 == str2, str1 is str2)
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
class Sub(Super):
    def __init__(self, name):
        super().__init__(name) # super function is used to access superclass
obj = Sub("Andy")
print(obj)
