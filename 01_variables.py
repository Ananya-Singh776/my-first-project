"""
==========================================================
PYTHON VARIABLES AND DATA TYPES
Author: Ananya Singh
==========================================================
"""

# Integer
age = 21
print("Age:", age)

# Float
cgpa = 8.24
print("CGPA:", cgpa)

# String
name = "Ananya Singh"
print("Name:", name)

# Boolean
placed = False
print("Placed:", placed)

# Multiple Assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Same value assignment
a = b = c = 100
print(a, b, c)

# Type Checking
print(type(age))
print(type(cgpa))
print(type(name))

# Dynamic Typing
data = 100
print(data)

data = "Python"
print(data)

# Type Casting
marks = "95"
marks = int(marks)
print(marks)

percentage = float(marks)
print(percentage)

# User Input
city = input("Enter your city: ")
print("City:", city)

# Constants
PI = 3.14159
print(PI)

# Swapping Variables
num1 = 10
num2 = 20

num1, num2 = num2, num1

print("After Swapping")
print(num1)
print(num2)

# Memory Address
number = 50
print(id(number))

# Deleting Variable
temp = 999
del temp

print("Variables Program Completed Successfully")
