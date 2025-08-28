# example - codes

# 1

# numbers = (1, 2, -5)
# print(numbers)

# 2

# a_tuple = (0, [1, 2, 3], (4, 5, 6), 7.0)
# print(a_tuple)

# 3

# languages = ('Python', 'Swift', 'C++')
# languages = ('Python', 'Swift', 'C++')
# # access the first item
# print(languages[0])   # Python

# 4

# cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# print('Total Items:', len(cars))

# 5

# a = tuple(range(5))
# print(a)
# b = tuple(range(5,10))
# print(b)
# c = tuple(range(0,10,2))
# print(c)
# d = tuple(range(10,0,-2))
# print(d)

# 6

# t1 = (2,3,4,5)
# print(sum(t1))

# 7

# t3 = (3,4,4,2,2,3,6,7,4,4)
# print(t3.count(4))

# 8

# t3 = (3,4,4,2,2,3,6,7,4,4)
# print(t3.index(2))
# print(t3.index(4,3,9))

# 9

# t3 = (3,4,4,2,2,3,6,7,4,4)
# print(min(t3))

# 10

# numbers = (7, 2, 8, 5, 9)
# print(max(numbers))

# 11

# a = (5,6,7,5,5,9,7)
# b = ("a","b","v","b")
# my_tu_1 = tuple(dict.fromkeys(a))
# print(my_tu_1)
# my_tu_2 = tuple(dict.fromkeys(b))
# print(my_tu_2)

# 12

# first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
# last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
# ages = (49, 55, 39, 33)
# zipped = tuple(zip(first_names, last_names,ages))
# print(zipped)

# 13

# b = ((1,2),(3,4),(5,6))
# my = tuple(item for l in b for item in l)
# print(my)

# post-labs

# pl-1

# Tuple = (1,2,4,5,6,6,6,6)

# print(Tuple.count(6))

# pl-2

# n=7

# Tuple = (1,2,4,5,6,6,6,6)

# count = Tuple.count(n)

# if(count==0) :
#     print(n,"is not there in tuple")
# else :
#     print(n,"is there in the tuple")

# pl-3

# t1 = (1234,5678)
# t1 = str(t1)
# print(t1,type(t1))

# pl-4

# t1 = (1234,5678,7,8,91)
# print("max = ",max(t1),"min = ",min(t1))

# pl-5

# tuple_of_strings = ('Hello', 'world', 'this', 'is', 'Python')

# single_string = ' '.join(tuple_of_strings)

# print("Single string:", single_string)


# pl-6

# t2 = (1,2,35,7,84,2,365,42,2321)
# t2 = list(t2)
# t2 = sorted(t2)
# t2 = tuple(t2)
# print(t2)

# pl-7

t3 = (range(0,9))
print("First element is",t3[0],"Last element is",t3[-1] )