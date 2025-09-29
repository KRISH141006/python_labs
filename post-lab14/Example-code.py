# 1

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  
#         self.model = model  

#     def car_details(self):
#         return f"Car: {self.brand}, Model: {self.model}"

# my_car = Car("Toyota", "Corolla")
# print(my_car.car_details())  

# 2

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# rect = Rectangle(10, 5)

# print(f"Area: {rect.area()}")  
# print(f"Perimeter: {rect.perimeter()}")  

# 3

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance

# # Create an account
# account = BankAccount("John", 1000)
# account.deposit(500)
# print(account.get_balance())  
# account.withdraw(700)
# print(account.get_balance())  

# 4

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "I am an animal."

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  
# print(cat.speak())  

# 5

# class Polygon:
#     def render(self):
#         print("Rendering Polygon...")

# class Square(Polygon):
#     def render(self):
#         print("Rendering Square...")

# class Circle(Polygon):
#     def render(self):
#         print("Rendering Circle...")
    
# s1 = Square()
# s1.render()

# c1 = Circle()
# c1.render()

# 6

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")  # 
