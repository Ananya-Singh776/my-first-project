"""
=========================================================
PYTHON FUNCTIONS
Author: Ananya Singh
=========================================================
"""

print("\n========== SIMPLE FUNCTION ==========\n")

def greet():
    print("Welcome to Python!")

greet()

print("\n========== FUNCTION WITH PARAMETERS ==========\n")

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Ananya")

print("\n========== RETURN VALUE ==========\n")

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

print("\n========== DEFAULT PARAMETERS ==========\n")

def student(name, course="CSE"):
    print(f"Name: {name}")
    print(f"Course: {course}")

student("Ananya")
student("Rahul", "ECE")

print("\n========== KEYWORD ARGUMENTS ==========\n")

def employee(name, salary):
    print(f"Name: {name}")
    print(f"Salary: {salary}")

employee(salary=50000, name="Aman")

print("\n========== ARBITRARY ARGUMENTS (*args) ==========\n")

def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90, 78, 88)

print("\n========== KEYWORD ARBITRARY ARGUMENTS (**kwargs) ==========\n")

def profile(**details):
    for key, value in details.items():
        print(key, ":", value)

profile(Name="Ananya", Age=21, City="Noida")

print("\n========== RECURSION ==========\n")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

print("\n========== LAMBDA FUNCTION ==========\n")

square = lambda x: x * x

print(square(9))

print("\n========== MAP FUNCTION ==========\n")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))

print(squares)

print("\n========== FILTER FUNCTION ==========\n")

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

print("\n========== LOCAL VARIABLE ==========\n")

def demo():
    message = "Inside Function"
    print(message)

demo()

print("\n========== GLOBAL VARIABLE ==========\n")

count = 10

def show():
    global count
    count += 5
    print(count)

show()

print("\n========== DOCSTRING ==========\n")

def multiply(a, b):
    """
    Returns multiplication of two numbers.
    """
    return a * b

print(multiply(4, 5))
print(multiply.__doc__)

print("\n========== TYPE HINTS ==========\n")

def divide(a: float, b: float) -> float:
    return a / b

print(divide(20, 4))

print("\n========== NESTED FUNCTION ==========\n")

def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()

print("\n========== FUNCTION AS ARGUMENT ==========\n")

def operation(a, b, func):
    return func(a, b)

print(operation(10, 5, add))

print("\n========== PRACTICE PROGRAM ==========\n")

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

for i in range(1, 21):
    if is_prime(i):
        print(i, end=" ")

print("\n")

print("========== END OF PROGRAM ==========")
