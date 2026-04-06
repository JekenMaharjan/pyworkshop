# ===============================================================
# LIST PRACTICE
# ===============================================================

# 1. Find largest element in list
list = [2, 4, 1, 5, 22, 33, 12, 41, 32, 40]
largest = list[0]

for num in list:
    if (num > largest):
        largest = num

print(f"Largest element in list is {largest}")

# ---------------------------------------------------------------

# 2. Find smallest element in list
list = [2, 4, 1, 5, 22, 33, 12, 41, 32, 40]
smallest = list[0]

for num in list:
    if (num < smallest):
        smallest = num

print(f"Smallest element in list is {smallest}")

# ---------------------------------------------------------------

# 3. Remove duplicates from list
list = [2, 1, 4, 5, 2, 3, 6, 2, 23, 4]
unique_list = []

for num in list:
    if num not in unique_list:
        unique_list.append(num)

print(f"List after removing duplicates is '{unique_list}'")

# set does remove duplicates but also changes order
# remove_duplicates = set(list)
# print(f"List after removing duplicates is '{remove_duplicates}'")

# ---------------------------------------------------------------

# 4. Sort list without using sort()
numbers = [5, 2, 9, 1, 7, 3]

# Bubble Sort
# for i in range(len(numbers)):
#     for j in range(0, len(numbers) - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

n = len(numbers)

for i in range(n):
    for j in range(n - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

# ---------------------------------------------------------------

# 5. Find second largest element
numbers = [2, 55, 1, 21, 14, 5]

sorted_number = sorted(numbers)
print(sorted_number)
print(f"Second largest number is {sorted_number[-2]}")

# largest = 0
# second_largest = 0

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest:
#         second_largest = num

# print(f"Second largest number is {second_largest}")

# ---------------------------------------------------------------

# 6. Merge two lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

merge_list = list1 + list2

print(f"Merged two lists : {merge_list}")

# ---------------------------------------------------------------

# 7. Count occurrences of element
numbers = [2, 3, 5, 2, 5, 3, 6, 2, 4, 2, 5]

count = {}

print("Count occurences of element are:")

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)

# ---------------------------------------------------------------

# 8. Reverse list
list = [2, 5, 22, 1, 7]

reversed_list = list[::-1]
print(f"Reversed list : {reversed_list}")


# ===============================================================
# LIST COMPREHENSIONS
# ===============================================================

# List comprehension is a short way to create lists.

# Normal Way:
numbers = [1, 2, 3, 4, 5]

squared = []

for num in numbers:
    squared.append(num ** 2)

print(squared)

# List Comprehension Way:
numbers = [1, 2, 3, 4, 5]

squared = [num ** 2 for num in numbers]

print(squared)

# ---------------------------------------------------------------

# Structure of List Comprehension:

# [expression for item in iterable]
# Example:
# [num ** 2 for num in numbers]
# 1. expression → num ** 2
# 2. item → num
# 3. iterable → numbers

# List Comprehension with Condition (if) : [expression for item in iterable if condition]

# ---------------------------------------------------------------

# Q1. Create a list of numbers from 1 to 5 using list comprehension.
# Expected Output: [1, 2, 3, 4, 5]
numbers = [i for i in range(1, 6)]

print(numbers)


# Q2. Multiply numbers by 2
numbers = [1, 2, 3, 4, 5]

numbers_X2 = [num * 2 for num in numbers]

print(numbers_X2)


# Q3. Create a list of squares from 1 to 6
square_list = [num ** 2 for num in range(1, 7)]

print(square_list)


# Q4. Create a list of even numbers from 1 to 10
even_numbers = [num for num in range(1, 11) if num % 2 == 0]

print(even_numbers)


# Q5. Create a list from 1 to 8 : If number is even → "Even" & If number is odd → "Odd"
even_odd_numbers = ["Even" if num % 2 == 0 else "Odd" for num in range(1, 9)]

print(even_odd_numbers)


# Q6. Create a list of numbers from 1 to 15. Only include numbers divisible by 3
div_3_numbers = [num for num in range(1, 16) if num % 3 == 0]

print(div_3_numbers)


# Q7. Convert this list to uppercase using list comprehension:
# fruits = ["apple", "banana", "mango", "orange"]
fruits = ["apple", "banana", "mango", "orange"]

upper_fruits = [fruit.upper() for fruit in fruits]

print(upper_fruits)


# Q8. Flatten this 2D list using nested list comprehension:
# matrix = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

flat_list = [num for row in matrix for num in row]

print(flat_list)


# Q9. Flatten this 2D list but keep only even numbers:
# matrix = [
#     [11, 12],
#     [13, 14],
#     [15, 16]
# ]
matrix = [
    [11, 12],
    [13, 14],
    [15, 16]
]

flat_list_even = [num for row in matrix for num in row if num % 2 == 0]

print(flat_list_even)


# Q10. Create a 3x3 multiplication table as a list of lists using nested list comprehension.
multiplication_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print(multiplication_table)




