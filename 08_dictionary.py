# ===============================================================
# DICTIONARY PRACTICE
# ===============================================================

# 1. Create dictionary of student marks
students = {
    "Jeken": {"Math": 85, "Science": 90},
    "Ram": {"Math": 70, "Science": 75},
    "Hari": {"Math": 80, "Science": 85}
}

print(students)

# ---------------------------------------------------------------

# 2. Find highest marks
students = {
    "Jeken": {"marks": 85},
    "Ram": {"marks": 70},
    "Hari": {"marks": 80}
}

# Extract all marks
marks = [info["marks"] for info in students.values()]

# Find highest
highest = max(marks)

print(f"Highest marks: {highest}")

# ---------------------------------------------------------------

# 3. Sort dictionary by values
students = {
    "Jeken": 85,
    "Ram": 70,
    "Hari": 90,
    "Sita": 75
}

sorted_students = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
print(sorted_students)

# ---------------------------------------------------------------

# 4. Merge two dictionaries
fruits1 = {
    "orange": 100,
    "banana": 120
}

fruits2 = {
    "apple": 150,
    "grapes": 200
}

merge_dict = fruits1 | fruits2
print(merge_dict)

# ---------------------------------------------------------------

# 5. Count frequency of characters
text = "hello world"

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)

# ---------------------------------------------------------------