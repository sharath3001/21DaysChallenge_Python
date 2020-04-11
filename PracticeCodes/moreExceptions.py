def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else: # only executes when try executes all statements without executing except
        print("Everything went fine")
    finally: # always executes
        print("It's time to say goodbye")
        return n
print(reciprocal(2))
print(reciprocal(0))
try:
    i = int("Hello!")
except Exception as e: # Exception is class
    print(e)
    print(e.__str__())
def printargs(args):
	lng = len(args)
	if lng == 0:
		print("")
	elif lng == 1:
		print(args[0])
	else:
		print(str(args))
try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=' : ' ,end=' : ')
	printargs(e.args)
try:
	raise Exception("my exception")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)
try:
	raise Exception("my", "exception")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)
class MyZeroDivisionError(ZeroDivisionError): # custom exception
	pass
def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("some worse news")
	else:		
		raise ZeroDivisionError("some bad news")
for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('Division by zero')
for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero')
	except ZeroDivisionError:
		print('Original division by zero')
