"""
=========================================================
PYTHON LOOPS
Author: Ananya Singh
=========================================================
"""

print("\n========== FOR LOOP ==========\n")

for i in range(1, 6):
    print(i)

print("\n========== WHILE LOOP ==========\n")

count = 1

while count <= 5:
    print(count)
    count += 1

print("\n========== BREAK ==========\n")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("\n========== CONTINUE ==========\n")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("\n========== PASS ==========\n")

for i in range(5):
    if i == 3:
        pass
    print(i)

print("\n========== NESTED LOOPS ==========\n")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("\n========== MULTIPLICATION TABLE ==========\n")

number = 7

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n========== SUM OF NUMBERS ==========\n")

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

print("\n========== FACTORIAL ==========\n")

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

print("\n========== FIBONACCI SERIES ==========\n")

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

print()

print("\n========== PRIME NUMBER ==========\n")

num = 29
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")

print("\n========== STAR PATTERN ==========\n")

rows = 5

for i in range(1, rows + 1):
    print("*" * i)

print("\n========== INVERTED STAR PATTERN ==========\n")

for i in range(rows, 0, -1):
    print("*" * i)

print("\n========== PYRAMID ==========\n")

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

print("\n========== REVERSE NUMBER ==========\n")

number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print(reverse)

print("\n========== PALINDROME NUMBER ==========\n")

number = 121
temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if number == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

print("\n========== ARMSTRONG NUMBER ==========\n")

number = 153
temp = number
digits = len(str(number))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == number:
    print("Armstrong Number")
else:
    print("Not Armstrong")

print("\n========== GUESSING GAME ==========\n")

secret = 8
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))

print("Correct!")

print("\n========== END OF PROGRAM ==========")
