# ===============================================================
# FUNCTIONS PRACTICE
# ===============================================================

# 1. Create function to add two numbers
def add_two_num(a, b):
    return a + b

print(add_two_num(15,5))

# ---------------------------------------------------------------

# 2. Function to check prime number
def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(check_prime(7))
    
# ---------------------------------------------------------------

# 3. Function to find factorial
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

print(factorial(5))
    

# ---------------------------------------------------------------

# 4. Function to reverse string
def reverse_string(str):
    rev = str[::-1]
    return rev

print(reverse_string("Permanent"))

# ---------------------------------------------------------------

# 5. Function to find maximum number
def max_num(list):
    sorted_list = sorted(list)
    max = sorted_list[-1]
    return max

print(max_num([2,1,3,6,11,44,5,30,40]))

# ---------------------------------------------------------------

# 6. Function to check palindrome
def check_palindrome(str):
    str = str.lower()
    str1 = str
    str2 = str[::-1]
    is_palindrome = True
    
    if (str1 == str2):
        is_palindrome = True
    else:
        is_palindrome = False
    
    return is_palindrome

print(check_palindrome("Madam"))

# ---------------------------------------------------------------