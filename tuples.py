"""
Tuples are unchangable. they are written in () brackets. 
tuple() constructor can be used to make a tuple. 

"""

b = ("apple", "banana", "cake")
print(b)


"Updating a tuple"

#convert tuple to list
x = ("apple", "banana", "coffee")
y = list(x)

y[0] = 'kiwi'

x = tuple(y)
print(x)

# Tuples are unchangeable therefore will need to be changed to list always before modifying it. 

"Unpacking a Tuple"
fruits = ("apple", "banana", "chocolate")

(red, green, blue) = fruits

print(red)
print(green)
print(blue)

"Using an '*' to the variable name will assign the variable with the rest of the tuple as a list"

grocery = ("apple", "banana", "cherry", "strawberry", "raspberry")

(red, green, *blue) = grocery

print(*blue)