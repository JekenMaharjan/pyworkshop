# ==================================================================
# WORKING WITH FILES
# ==================================================================

# Opening a File

# Python uses the open() function to open a file.
# Syntax:
file = open("filename.txt", "mode")
# "r" → read (default)
# "w" → write (overwrite)
# "a" → append
# "x" → create new file (fails if exists)
# "b" → binary mode (for images, etc.)

# -------------------------------------------------------------------

# Reading a File

# Suppose we have a file example.txt:
# Hello World
# Python is fun
# Example:
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Note:
# 1. file.read() → reads whole content
# 2. Always close the file with file.close()

# -------------------------------------------------------------------

# Writing to a File

file = open("example.txt", "w")
file.write("This is my first file writing.\nPython is amazing!!")
file.close
# Note: "w" → creates new file or overwrites existing

# -------------------------------------------------------------------

# Appending to a File

file = open("exmaple.txt", "a")
file.write("\nAdding one more line.")
file.close()
# Note: "a" → adds content without removing old content

# -------------------------------------------------------------------

# Reading Line by Line

file = open("example.txt", "r")
for line in file:
    print(line.strip()) # .strip() removes extra newlines
file.close()


# Using 'with' Statement

# 'with' automatically closes the file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# -------------------------------------------------------------------

# File Positioning

# Move cursor in file:
file.seek(0)   # Go to start
file.seek(5)   # Go to 5th byte/character

# Check cursor position:
pos = file.tell()
print(pos)

# ==================================================================
# PRACTICE QUESTIONS
# ==================================================================

# 1. Create a file called myfile.txt and write your name and age in it.
with open("myfile.txt", "w") as file:
    file.write("Jeken Maharjan - 25")

# 2. Append your favorite programming language to the file.
with open("myfile.txt", "a") as file:
    file.write("\nPYTHON")

# 3. Read the file and print each line.
with open("myfile.txt", "r") as file:
    for line in file:
        print(line.strip())


