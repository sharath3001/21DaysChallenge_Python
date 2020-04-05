import math
print(math.sin(math.pi/2))

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
pi = 3.14
print(sin(pi/2)) # our variable and function
print(math.sin(math.pi/2)) # math module's variable and function
from math import sin, pi # import only what is required
print(sin(pi/2))

# from module import *
# to import all entities above statement is used

# import module as alias
# aliasing module or giving our own name
import math as m # math keyword cannot be used now
print(m.sin(m.pi/2))

from math import pi as PI, sin as sine
print(sine(PI/2))
