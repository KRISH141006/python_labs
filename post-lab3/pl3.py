#example code

#1

# # create a string using double quotes
# string1 = "ICT Department"
# print(string1)
# # create a string using single quotes
# string1 = ' ICT Department '
# print(string1)

# 2

# string2 = '3EK1'
# # access 1st index element
# print(string2 [1])

# 3

# string3 = 'ICT Department'
# # access 4th last element
# print(string3 [-4]) 

# 4

# string4 = 'ICT Department'
# # access character from 1st index to 3rd index
# print(string4[1:4])  

# # 5
# print(string4[:2])
# print(string4[2:])

# 6

# message = 'ICT Department'
# message[0] = 'H'
# print(message)

# 7
# message = 'ICT'
# # assign new string to message variable
# message = 'ICT Department'
# print(message)

# 8

# message = """
# ICT
# Department
# 3EK1
# """
# print(message)

# 9

# str1 = "ICT"
# str2 = "Department"
# str3 = "3EK1"
# # compare str1 and str2
# print(str1 == str2)
# # compare str1 and str3
# print(str1 == str3)

# 10

# greet = "ICT"
# name = "Department"
# # using + operator
# result = greet + name
# print(result)

# 11

# greet = 'ICT'
# # count length of greet string
# print(len(greet))

# 12

# program = "apple"
# battle = "battle at france"

# print('a' in program)
# print('at' not in battle)

# 13

# message = 'python is fun'
# # convert message to uppercase
# print(message.upper())

# 14

# message = 'PYTHON IS FUN'
# # convert message to lowercase
# print(message.lower())

# 15

# text = 'CE Department'
# replaced_text = text.replace('CE', 'ICT')
# print(replaced_text)

# 16

# message = 'Python is a fun programming language'
# # check the index of 'fun'
# print(message.find('fun'))

# 17

# title = 'Python Programming   '
# result = title.rstrip()
# print(result)

# 18

# text = 'Python is fun'
# # split the text from space
# print(text.split())

# 19

# message = 'Python is fun'
# # check if the message starts with Python
# print(message.startswith('Python'))

# 20

# pin = "523"
# # checks if every character of pin is numeric 
# print(pin.isnumeric())

# 21

# text = 'Python is fun'
# # find the index of is
# result = text.index('is')
# print(result)

# 22

# name = 'Cathy'
# country = 'UK'
# print(f'{name} is from {country}')

# 23

# str = "This is a \n normal string example" 
# print(str) 
# raw_str = r"This is a \n raw string example" 
# print(raw_str)

# Post-labs

# 1

# string = 'apple'
# str = string[::-1]
# print(string)
# print(str)

# 2

# string1 = 'apple'
# string2 = 'navjvan'
# print(string1==string1[::-1])
# print(string2==string2[::-1])

# 3

# string1 = '12345'
# string2 = 'apple'
# print(string1.isdigit())
# print(string2.isdigit())

# 4

# string = 'Earth goes round the sun .'
# string1 = string.split()
# length = 0
# word = 0
# for i in string1 :
#     if length<len(i) :
#         length = len(i)
#         word = i

# print("longest word =",word)

# 5

string = 'Earth goes round the sun .'
string1 = string.split()
length = len(string1[len(string1)-2])

print(length)

