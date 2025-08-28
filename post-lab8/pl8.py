# example codes

# 1

# def add(a,b):
#      result = a+b
#      return result

# import pl8 as addition
# a = addition.add(4,5)
# print(a)

# 2

# import math
# # use math.pi to get value of pi
# print("The value of pi is", math.pi)

# 3

# # import module by renaming it
# import math as m
# print(m.pi)

# 4

# # import only pi from math module
# from math import pi
# print(pi)

# 5

# # import all names from the standard module math
# from math import *
# print("The value of pi is", pi)

# 6

# import math
# print(dir(math))

# 7

# help('modules')

# 8

# import math
# r=14
# area = math.pi * (r**2)
# print(area)

# 9

# import math 
# print (math.inf) 
# print (-math.inf)

# post-labs

# pl-1

# import math

# def degrees_to_radians(degrees):
#     return degrees * (math.pi / 180)

# degrees = 180
# radians = degrees_to_radians(degrees)
# print(f"{degrees} degrees is {radians} radians")

# pl-2

# import math

# x = 2  
# y = 6 * x**2 + 4 * math.sin(x)
# print(f"y = {y}")

# pl-3

import math

def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

# Evaluate at x = π
x = math.pi
results = evaluate_functions(x)
print(f"f(x) = {results[0]}")
print(f"f'(x) = {results[1]}")
print(f"f''(x) = {results[2]}")
