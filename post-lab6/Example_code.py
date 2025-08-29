# example-codes

# 1

x = 10
if x>5:
    print("x is greter than 5")

# 2

x = 10
if  x>5 :
    print('x is greater than 5')
elif x ==5:
   print('x is equal to 5')
else:
   print('x is less than 5')

# 3

x = 10
if  x>5 :
    print('x is greater than 5')
else:
   print('x is less than 5')

# 4

age = 35

if age >= 60:
    print("You are a senior citizen.")
else:
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a teenager.")

# 5

num = 10

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive but odd.")
else:
    print("The number is not positive.")

# 6

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
      print(fruit)

# 7 - while loop example

x = 1
while x<=5:
     print(x)
     x+=1

# 8

for x in range(1,6):
	if x==3:
	    break 
print(x)

# 9

for x in range(1,6):
    if x == 3:
        pass
    print(x)

# 10 try-catch block

try:
  number = int(input("Enter a number: "))
  result = 10 / number
  print("The result is:", result)
except ZeroDivisionError:
  print("Division by zero is not allowed.")
except ValueError:
  print("Invalid input. Please enter a valid number.")

# 11

add = lambda x, y: x + y
print(add(3, 5))  

# 12

def factorial(n) :
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 

