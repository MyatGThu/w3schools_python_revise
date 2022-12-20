"""Looping through the list"""
thislist = ['apple', 'banana', 'cherry']
for x in thislist:
    print(x)

"""Looping at specific index"""
for i in range((len(thislist))):
    print(thislist[2] + '\n')

"""While lopps for list"""

i == 0
while i < len(thislist):
    print(thislist[i] + '\n')
    i = i + 1

"""Offers the shortest syntax to print all items in a list"""
[print(x) for x in thislist]