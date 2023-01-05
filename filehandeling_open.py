# File Handeling

# open() function -  2 parameters { filename and mode }

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""


f = open("demofile.txt")

f = open("demofile.txt", "rt")

# read() method for reading content of file.

print(f.read())

# return one line by using readline() method.

print(f.readline())
f.close() # close file after reading it.

