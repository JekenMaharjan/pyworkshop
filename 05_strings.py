# ===============================================================
# STRINGS PRACTICE
# ===============================================================

# 1. Reverse a string
str = "WorkShop"
char_list = list(str)
reverse_list = char_list[::-1]
# print(reverse_list)
reverse_str = ''.join(reverse_list)
print(f"Reverse of a string is {reverse_str}")

# ---------------------------------------------------------------

# 2. Check palindrome string
str = "Madam"
lower_str = str.lower()
reverse_str = lower_str[::-1]

if (lower_str == reverse_str):
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")

# ---------------------------------------------------------------

# 3. Count vowels in string
str = "Leopard"
vowels = "aeiouAEIOU"  # include uppercase vowels
count = 0

for char in str:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{str}' is {count}")

# ---------------------------------------------------------------

# 4. Count words in string
str = "The quick brown fox"
word_count = len(str.split())  # split by spaces
print(f"Words count in '{str}' is {word_count}")

# ---------------------------------------------------------------

# 5. Convert string to uppercase/lowercase
str = "GranDFaThEr"
upper_str = str.upper()
lower_str = str.lower()
print(f"Uppercase of '{str}' is {upper_str}")
print(f"Lowercase of '{str}' is {lower_str}")

# ---------------------------------------------------------------

# 6. Remove spaces from string
str = "This is my profile"
# space_removed_str = str.replace(" ", "")
space_removed_str = ''.join(str.split())  # split by spaces, then join without spaces
print(f"{space_removed_str}")

# ---------------------------------------------------------------

# 7. Find duplicate characters
str = "Aeroplane"
string = str.lower()
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print duplicate characters
print(f"Duplicate characters in the string '{str}' are:")
for char, count in char_count.items():
    if count > 1:
        print(char)

# ---------------------------------------------------------------

# 8. Check anagram strings
str1 = "listen"
str2 = "silent"

# Remove spaces and lowercase both strings (optional, for general cases)
str1_clean = str1.replace(" ", "").lower()
str2_clean = str2.replace(" ", "").lower()

# Check if sorted letters are the same
if sorted(str1_clean) == sorted(str2_clean):
    print(f"'{str1}' and '{str2}' are anagrams")
else:
    print(f"'{str1}' and '{str2}' are not anagrams")

# ---------------------------------------------------------------

# 9. Count characters/letters in string
str = "Elephant"
char_count = 0

for char in str:
    char_count += 1

print(f"Characters count in '{str}' is {char_count}")

# ---------------------------------------------------------------