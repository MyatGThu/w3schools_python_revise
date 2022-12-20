"""Slicing Strings"""

#prints out llo
b = "Hello World"

print(b[2:5])

"""Slicing from Start"""
#starts from the beginning of the string
print(b[:5])

"""Slicing to End"""

print(b[2:])

"""Reverse Slicing"""
#starts from the back of the string
print(b[-5:-2])

"""Removing whitespace in strings"""
b = " Hello, World! "
#output "Hello, World!"
print(b.strip())

"""Replacing Strings"""
#replaces the designated letter H with J.
print(b.replace("H","J"))

"""Split Strings"""
#prints out ['Hello', 'World!']
print(b.split(","))
