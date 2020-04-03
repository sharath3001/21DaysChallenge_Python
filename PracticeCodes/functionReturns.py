def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1)) # returns None (None value)

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()

def myFunction():
    print("Do I know that variable?", var) # scope of var makes it accessible inside function but if we declare same name variable then original var will be shadowed 
var = 1
myFunction()
print(var)

def myFunction():
    global var # will access the var declared outside the function and will not create a new one
    var = 2
    print("Do I know that variable?", var)
var = 1
myFunction()
print(var)

def myFunction(n):
    print("I got", n)
    n += 1
    print("I have", n)
var = 1
myFunction(var)
print(var) # var will not be changed

def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]
myList2 = [2, 3]
myFunction(myList2) # no effect on myList2 coz myList1 will be created new

def myFunction(myList1):
    print(myList1)
    del myList1[0]
myList2 = [2, 3]
myFunction(myList2)
print(myList2) # myList2 will be changed coz parameter is updated(only with list)
print(myList2)
