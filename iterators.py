"""
Iterator is an object that contains contable number of values.
Consists of methods __iter__() and __next()__
"""

# Objects have a iter() method to get an iterator

mytuple = ("cake", "carrots", "bread")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings can be returned as an iterator

mystr = "cake"
myit = iter(mystr)


print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 'for' loop for iterable objects

for x in mytuple:
  print(x)
