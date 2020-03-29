print(1==1)
var = 0
print(var == 0) # comparison/equality/equal to operator
var = 0
print(var != 0) # no equal to operator

# other comparison operators <,<=,>,>=

# choose the larger number
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2: larger_number = number1
else: larger_number = number2
larger_number = max(number1,number2) # another way
print("The larger number is:", larger_number)

# plant example
plant = input("Enter plant: ")
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not",plant)

# leap year example
year = int(input("Enter a year: "))
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
