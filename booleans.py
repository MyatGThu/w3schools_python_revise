"""Checking boolean values"""
print(10 > 9)
#prints out true
print(10 == 9)
#prints out false
print(10 < 9)
#prints out false


""" Most values are True except for empty strings, dict / tuples / sets / list and the number 0"""

class myclass():
  def __len__(self): #__len__ is to find the length of instance attributes
    return 0

myobj = myclass()
print(bool(myobj))

# Python also have build in method = "isinstance()". 

x = 200

print(isinstance(x,int))