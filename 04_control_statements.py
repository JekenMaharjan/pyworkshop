# ===============================================================
# CONTROL STATEMENTS (if-else, loops) PRACTICE
# ===============================================================

# 1. Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# ---------------------------------------------------------------

# 2. Print even numbers from 1 to 100
for i in range(1, 101):
    if (i % 2 == 0):
        print(i)

# ---------------------------------------------------------------

# 3. Print odd numbers from 1 to 100
for i in range(1, 101):
    if (i % 2 != 0):
        print(i)

# ---------------------------------------------------------------

# 4. Find sum of first N numbers
sum = 0
num = int(input("Enter value of N: "))

for i in range(0, num+1):
    sum += i

print(sum)

# ---------------------------------------------------------------

# 5. Find largest number in a list
list = [22,4,61,10,53,99,1,2,6]

# print(f"Largest number in a list is {max(list)}")

# OR

largest = list[0]

for num in list:
    if (num > largest):
        largest = num

print(largest)

# ---------------------------------------------------------------

# 6. Print Fibonacci series
n = 10  # number of terms
a, b = 0, 1
fib_series = []

for i in range(n):
    fib_series.append(a)
    a, b = b, a + b  # update a & b

print("Fibonacci series: ", fib_series)

# ---------------------------------------------------------------

# 7. Check if number is prime
num = 7
is_prime = True

if (num <= 1):
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# ---------------------------------------------------------------

# 8. Count digits in a number
num = 12534
count = 0

num_list = str(num)

for n in num_list:
    count = count + 1

print(f"Digits count in a number is {count}")

# ---------------------------------------------------------------

# 9. Reverse a number
num = 12345
rev = 0
original = num

while num > 0:
    digit = num % 10        # get the last digit
    rev = rev * 10 + digit  # append digit to reversed number
    num = num // 10         # remove last digit & '//' is Floor Division

print("Original number:", original)
print("Reversed number:", rev)

# ---------------------------------------------------------------

# 10. Check palindrome number
num = 12521
rev = 0
original = num
is_palindrome = True

while num > 0:
    digit = num % 10        # get the last digit
    rev = rev * 10 + digit  # append digit to reversed number
    num = num // 10         # remove last digit

print("Original number:", original)
print("Reversed number:", rev)

if(original == rev):
    is_palindrome = True
else:
    is_palindrome = False


if (is_palindrome == True):
    print(f"{original} is palindrome number")
else:
    print(f"{original} is not palindrome number")

# ---------------------------------------------------------------