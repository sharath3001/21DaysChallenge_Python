def ftintom(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def lbstokg(lb):
    return lb * 0.45359237
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: # \ is used to tell python that next line is continued and nothing should be there after \ not even comment
        return None
    return weight / height ** 2
print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))

# factorial
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
for n in range(1, 6): # testing
    print(n, factorialFun(n))

# fibonacci
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1
    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum
for n in range(1, 10): # testing
    print(n, "->", fib(n))

# fibonacci using recursion
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
for n in range(1, 10): # testing
    print(n, "->", fib(n))

# factorial using recursion
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)
for n in range(1, 6): # testing
    print(n, factorialFun(n))
