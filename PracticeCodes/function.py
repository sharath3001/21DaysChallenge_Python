def message(): # function without parameters
    print("Enter a value: ")
print("We start here.")
message()
print("We end here.")

def message(number): # function with parameter
    print("Enter a number:", number)
message(1)

def message(what, number): # function with multiple parameters and example of positional parameters also
    print("Enter", what, "number", number)
message("telephone", 11)
message("price", 5)
message("number", "number")

def introduction(firstName, lastName): 
    print("Hello, my name is", firstName, lastName)
introduction(firstName = "James", lastName = "Bond") # keyword arguments example
introduction(lastName = "Skywalker", firstName = "Luke")

def sum(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
sum(3, c = 1, b = 2) # mixing of both

def introduction(firstName, lastName="Smith"): # parameter with default value
    print("Hello, my name is", firstName, lastName)
introduction("Henry")
