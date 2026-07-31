"""
=========================================================
PYTHON CONDITIONAL STATEMENTS
Author: Ananya Singh
=========================================================
"""

print("========== IF Statement ==========")

age = 20

if age >= 18:
    print("Eligible to Vote")

print("\n========== IF-ELSE ==========")

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\n========== IF-ELIF-ELSE ==========")

marks = 82

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

print("\n========== Nested IF ==========")

username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

print("\n========== Ternary Operator ==========")

age = 17

result = "Adult" if age >= 18 else "Minor"
print(result)

print("\n========== Multiple Conditions ==========")

salary = 45000
experience = 3

if salary >= 40000 and experience >= 2:
    print("Eligible for Promotion")
else:
    print("Not Eligible")

print("\n========== Logical Operators ==========")

temperature = 35

if temperature > 30 or temperature < 10:
    print("Extreme Weather")

if not (temperature < 0):
    print("Temperature is above freezing")

print("\n========== Largest of Three Numbers ==========")

a = 50
b = 75
c = 60

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)

print("\n========== Leap Year Checker ==========")

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

print("\n========== Positive / Negative ==========")

num = -15

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

print("\n========== Calculator ==========")

num1 = 15
num2 = 5
operator = "+"

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")

print("\n========== Pass or Fail ==========")

subject1 = 78
subject2 = 85
subject3 = 66

average = (subject1 + subject2 + subject3) / 3

if average >= 40:
    print("PASS")
else:
    print("FAIL")

print("\n========== Discount Calculator ==========")

amount = 2500

if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 15
elif amount >= 1000:
    discount = 10
else:
    discount = 5

print("Discount:", discount, "%")

print("\n========== End of Program ==========")
