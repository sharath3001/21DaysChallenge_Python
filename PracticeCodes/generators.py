class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1
	def __iter__(self): # to return object and start iterator
		print("__iter__")		
		return self
	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret
for i in Fib(10):
	print(i)
class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1
	def __iter__(self):
		print("Fib iter")
		return self
	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret
class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter;
object = Class(8)
for i in object:
	print(i)
def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow # generator without iterator protocol
        pow *= 2
for v in powersOf2(8):
    print(v)
lst = []
for x in range(10):
    lst.append(1 if x % 2 == 0 else 0) # comprehensive way of if kind of operator
print(lst)
lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10)) # generator
for v in lst:
    print(v, end=" ")
print()
for v in genr:
    print(v, end=" ")
print()
def printfunction(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')
printfunction([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2) # lambda function
list1 = [x for x in range(5)]
list2 = list(map(lambda x: 2 ** x, list1)) # map function returns an iterator after applying all values of list on given function
print(list2)
for x in map(lambda x: x * x, list2):
	print(x, end=' ')
print()
from random import seed, randint
seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data)) # filter function only returns True values
print(data)
print(filtered)
def outer(par):
	loc = par
	def inner():
		return loc
	return inner
var = 1
fun = outer(var) # returns a function called closure
print(fun())
def makeclosure(par):
	loc = par
	def power(p):
		return p ** loc
	return power
fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))
