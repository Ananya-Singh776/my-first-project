"""
==========================================================
PYTHON OPERATORS
Author: Ananya Singh
==========================================================
"""

print("\n========== Arithmetic Operators ==========\n")

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("\n========== Assignment Operators ==========\n")

x = 10
print("Initial:", x)

x += 5
print("x += 5 :", x)

x -= 2
print("x -= 2 :", x)

x *= 3
print("x *= 3 :", x)

x /= 2
print("x /= 2 :", x)

x //= 2
print("x //= 2 :", x)

x %= 3
print("x %= 3 :", x)

print("\n========== Comparison Operators ==========\n")

num1 = 20
num2 = 15

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print("\n========== Logical Operators ==========\n")

age = 21
citizen = True

print(age >= 18 and citizen)
print(age < 18 or citizen)
print(not citizen)

print("\n========== Identity Operators ==========\n")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2)
print(list1 is list3)
print(list1 is not list2)

print("\n========== Membership Operators ==========\n")

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)

print("\n========== Bitwise Operators ==========\n")

x = 5
y = 3

print("AND:", x & y)
print("OR:", x | y)
print("XOR:", x ^ y)
print("NOT:", ~x)
print("Left Shift:", x << 1)
print("Right Shift:", x >> 1)

print("\n========== Operator Precedence ==========\n")

result = 5 + 2 * 3
print(result)

result = (5 + 2) * 3
print(result)

print("\n========== Practical Examples ==========\n")

length = 12
breadth = 8

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)
print("Perimeter =", perimeter)

salary = 50000
bonus = salary * 0.10

print("Bonus =", bonus)

marks = 88

print("Pass" if marks >= 40 else "Fail")

print("\n========== End of Program ==========")
