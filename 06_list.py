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

# ---------------------------------------------------------------

