# example codes

# 1

def add(a,b):
     result = a+b
     return result

import Example_code as addition
a = addition.add(4,5)
print(a)

# 2

import math
# use math.pi to get value of pi
print("The value of pi is", math.pi)

# 3

# import module by renaming it
import math as m
print(m.pi)

# 4

# import only pi from math module
from math import pi
print(pi)

# 5

# import all names from the standard module math
from math import *
print("The value of pi is", pi)

# 6

import math
print(dir(math))

# 7

help('modules')

# 8

import math
r=14
area = math.pi * (r**2)
print(area)

# 9

import math 
print (math.inf) 
print (-math.inf)

