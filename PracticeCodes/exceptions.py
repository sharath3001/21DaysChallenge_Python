firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
try:
    print(firstNumber / secondNumber)
except:
    print("This operation cannot be done.")
print("THE END.")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except: # if any other exception like KeyboardInterrupt occurs
    print("Oh dear, something went wrong...")
print("THE END.")

try:
    y = 1 / 0
except ArithmeticError: # super class of ZeroDivisionError
    print("Oooppsss...")
print("THE END.")
# except(exc1, exc2): will handle two exceptions

def badFun(n):
    raise ZeroDivisionError # explicitly raise exception
try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")
print("THE END.")

def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # can only be written inside except and raises the exception again
try:
    badFun(0)
except ArithmeticError:
    print("I see!")

import math
x = float(input("Enter a number: "))
assert x >= 0.0 # will raise an AssertionError if the result of expression is None i.e., not True or non zero number or string
x = math.sqrt(x)
print(x)
print("THE END.")
