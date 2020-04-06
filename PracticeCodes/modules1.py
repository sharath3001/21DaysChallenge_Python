import math
print(dir(math))
from math import pi, radians, degrees, sin, cos, tan, asin, e, exp, log
ad = 90
ar = radians(ad)
ad = degrees(ar)
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
print(pow(e, 1) == exp(log(e))) # pow() is in built
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

from random import random, randrange, randint, choice, sample # seed() function can be used to set seed
for i in range(5):
    print(random()) # 0.0<=i<1.0
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))

from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
for atr in python_version_tuple():
    print(atr)
