# Importing RegEx module
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# notation for reference https://www.w3schools.com/python/python_regex.asp

# findall() function.

x = re.findall("ai", txt)
print(x)

# If not found will print out an empty list.
x = re.findall("Portugal",txt)
print(x)

# search() function
x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())

# Prints out no match - None
x = re.search("Portugal",txt)
print(x)


# split() function
x = re.split("\s", txt) #spliting at each white-space character
print(x)

# You can control the split occurance by giving parameters
x = re.split("\s", txt, 1)
print(x)

# sub() function
x = re.sub("\s", "9", txt) #replaces white-space with '9'
print(x)

# You can also control the replacements by parameters
x = re.sub("\s", "9", txt, 2)
print(x)

# Matching Objects

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
