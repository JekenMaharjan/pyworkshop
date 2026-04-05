# ===============================================================
# SET PRACTICE
# ===============================================================

# 1. Find common elements in two sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 6, 7, 8}

print(f"Common elements in {set1} & {set2} are : ")
for i in set1:
    for j in set2:
        if i == j:
            print(i)

# ---------------------------------------------------------------

# 2. Remove duplicates using set
numbers = [1, 2, 3, 4, 5, 2, 4]

remove_duplicate = set(numbers)
print(f"After removed duplicates : {remove_duplicate}")

# ---------------------------------------------------------------

# 3. Find union and intersection
set3 = {1, 2, 3, 4, 5}
set4 = {1, 4, 5, 6, 7}

# Union
union = set3 | set4
print("Union : ", union)

# Intersection
intersection = set3 & set4
print("Intersection : ", intersection)

# ---------------------------------------------------------------