

file1 = open("./FileHandles/file1.txt", "r")
content = file1.read()
print(content)
# Reads the entire file as one string (including \n for line breaks).
# content = file1.readline()
# print(content)
# content = file1.readlines()
# print(content)
# Reads the entire file but returns a list of lines, each line as a string including the \n.
file1.close()


# content = file1.read()
# content = file1.readlines()
# After .read(), the file pointer is at the end of the file, so the next .readlines() will return an empty list.


# Writing to a file

# file = open("./FileHandles/file1.txt", "w")

# file.write("This is a new line.\n")
# file.write("This is another line.\n")
# file.close()

# file = open("./FileHandles/sample.txt", "w")

# file.write("This is a sample file.\n")
# file.write("It contains some text.\n")
# file.close()

# file = open("./FileHandles/sample.txt", "r")
# file_content = file.readlines()
# print(len(file_content))  # Output: 2 (number of lines in the file)
# file.close()


# Appending to a file



file = open("./FileHandles/sample.txt", "a")
file.write("This line is appended to the file.\n")
file.write("Another line is appended.\n")
file.write("Appending more text to the file.\n")
file.close()


file = open("./FileHandles/sample.txt", "r")
file