# ===============================================================
# Simple Password Generator
# ===============================================================

import random
import string

# Define password length
length = 10

# Define characters to use
chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(chars) for _ in range(length))  # _ is a throwaway variable

# Print password
print("Generated Password:", password)