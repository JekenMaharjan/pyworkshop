# ===============================================================
# PYTHON BASICS
# ===============================================================

# 1. Print "Hello, World!" in Python
print("Hello, World!")

# ---------------------------------------------------------------

# 2. Take user input and print it
username = input("Enter username: ")
print(f"Your username is {username}")

# ---------------------------------------------------------------

# 3. Add two numbers entered by user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"Addition of {a} & {b} is {a+b}")

# ---------------------------------------------------------------

# 4. Swap two variables (without third variable)
a = 5
b = 10

print("Before Swapping:")
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a

print("After Swapping:")
print(f"a = {a}")
print(f"b = {b}")

# ---------------------------------------------------------------

# 5. Find largest of 3 numbers
a = 10
b = 11
c = 6

# print(max(a, b, c))

# OR

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print(largest)

# ---------------------------------------------------------------

# 6. Check if number is even or odd
num = 9

if (num % 2 == 0):
    print("Even")
else:
    print("Odd")

# ---------------------------------------------------------------

# 7. Check if number is positive, negative, or zero
num = -12

if (num > 0):
    print("Positive")
elif (num < 0):
    print("Negative")
else:
    print("Zero")

# ---------------------------------------------------------------

# 8. Find factorial of a number
num = 5
fact = 1

# for i in range(1, num+1):
# OR
for i in range(num, 0, -1): # range(start, stop, step)
    fact *= i

print(fact)

# ---------------------------------------------------------------

# 9. Print multiplication table of a number
num = 2

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")

# ---------------------------------------------------------------

# 10. Calculate simple interest
P = 24000
R = 5
T = 4

SI = (P * R * T) / 100

print(f"Simple Interest is {SI}")

# ---------------------------------------------------------------
