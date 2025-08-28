# example-codes

# 1

# x = 10
# if x>5:
#     print("x is greter than 5")

# 2

# x = 10
# if  x>5 :
#     print('x is greater than 5')
# elif x ==5:
#    print('x is equal to 5')
# else:
#    print('x is less than 5')

# 3

# x = 10
# if  x>5 :
#     print('x is greater than 5')
# else:
#    print('x is less than 5')

# 4

# age = 35

# if age >= 60:
#     print("You are a senior citizen.")
# else:
#     if age >= 18:
#         print("You are an adult.")
#     else:
#         print("You are a teenager.")

# 5

# num = 10

# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive but odd.")
# else:
#     print("The number is not positive.")

# 6

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#       print(fruit)

# 7 - while loop example

# x = 1
# while x<=5:
#      print(x)
#      x+=1

# 8

# for x in range(1,6):
# 	if x==3:
# 	    break 
# print(x)

# 9

# for x in range(1,6):
#     if x == 3:
#         pass
#     print(x)

# 10 try-catch block

# try:
#   number = int(input("Enter a number: "))
#   result = 10 / number
#   print("The result is:", result)
# except ZeroDivisionError:
#   print("Division by zero is not allowed.")
# except ValueError:
#   print("Invalid input. Please enter a valid number.")

# 11

# add = lambda x, y: x + y
# print(add(3, 5))  

# 12

# def factorial(n) :
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5)) 

# post-labs

# pl1

# i=1

# while i<=100 :
#     if i%2!=0 :
#         print(i)
    # i+=1

# pl2

# n=35

# sum_to_n = (n*(n+1)/2)

# print(sum_to_n)

# pl3

# n = 123
# def numOfDigits(n) :
#     count = 0
#     while (n>0) :
#         n = n//10
#         count +=1
#     return count

# print(numOfDigits(n))

# pl4

# n = 123
# n = str(n)

# print(n[0],n[len(n)-1])

# pl5

# n = 1243
# n = str(n)
# n_list = list(n)
# temp = n_list[0]
# n_list[0] = n_list[len(n)-1]
# n_list[len(n)-1] = temp

# n = int("".join(n_list))
# print(n)

# pl6

# n = 1234
# mul = 1

# while(n>0) :
#     rem = n%10
#     n = n//10
#     mul = mul * rem

# print(mul)

# pl7

n = 1234
rev = 0

while(n>0) :
    rem = n%10
    n = n//10
    rev = rev * 10 + rem

print(rev)


