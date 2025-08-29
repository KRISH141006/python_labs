# example codes

# 1

ages = [19, 26, 29]
print(ages)

# 2

a = list(range(5))
print(a)

# 3

b = list(range(5,10))
print(b)

# 4

c = list(range(0,10,2))
print(c)

# 5

d = list(range(10,0,-2))
print(d)

# 6

List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)

# 7

List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2, 10087)
print(List)

# 8

List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
# Add List2 to List1
List1.extend(List2)
print(List1)

# 9

List = [1, 2, 3, 4, 5]
print(sum(List))

# 10

List = ['gfg', 'abc', 3]
print(sum(List))

# 11

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

List = ['a','b','c','d','a']
print(List.count('a'))

# 12

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))

# 13

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

# 14

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2, 2))

# 15

numbers = [5, 2, 8, 1, 9]
print(min(numbers))

# 16

numbers = [5, 2, 8, 1, 9]
print(max(numbers))

# 17

List = [2.3,4.445,3,5.33,1.054,2.5]
List.sort()
print(List)

# 18

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
#Reverse flag is set True
List.sort(reverse=True)
print(List)

# 19

# creating a list
list = [1,2,3,4,5]
#reversing the list
list.reverse()
#printing the list
print(list)

# 20

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())

# 21

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(0))

# 22

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

# 23

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

# 24

my_list_1 = [5, 2, 90, 24, 10, 2, 90, 34]
my_list_2 = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']

# removing duplicates from list 1
my_list_1 = list(dict.fromkeys(my_list_1))
print(my_list_1)

# 25
my_list_2 = list(dict.fromkeys(my_list_2))
print(my_list_2)

# 26

# combing lists with the help of zip() function
my_list_1 = [5, 2, 90, 24, 10]
my_list_2 = [6, 3, 91, 25, 12]

# combined
my_combined_list = list(zip(my_list_1, my_list_2))
print(my_combined_list)

# 27

my_list = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']
most_frequent_value = max(set(my_list), key=my_list.count)
print("The most common element is:", most_frequent_value)

# 28

list_of_lists = [[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]
# using list comprehension
my_list = [item for List in list_of_lists for item in List]
print(my_list)