"""Strings are Arrays"""

a = "Hello World"
#Will print out the letter 'e'.
print(a[1])

"""Loop through strings"""

for x in "Hello World":
    #prints out each letters of string until its completed
    print(x)

"""Finding out length of a string"""

#Python will count the length of letters in the string. (this include spaces)
print(len(a))

"""Checking for letters/words in strings"""

txt = "Free stuff are best."
print('Free' in txt)

#using 'if' loop

if 'Free' in txt:
    print("Yes, 'Free' is present.")

"""Check if Not"""

print('expensive' not in txt)
if 'expensive' not in txt:
    print("No, 'exepsnive' is not found.")