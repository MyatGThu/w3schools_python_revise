fruits = ['apple', 'banana', 'grapes']
for y in fruits:
    print(y)

"looping through a string"

for x in "banana":
    print(x)

"break statement"

for x in fruits:
    print(x) #goes all the way to banana
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x) #stops at apple

"continue statement"

for x in fruits:
    if x == "apple":
        continue
    print(x)

#range() function

for x in range(6):
    print(x)

print("\n")
for x in range(2,6):
    print(x)

#incrementing value by adding a 3rd parameter
print("\n")
for x in range(2,30, 3):
    print(x)

#else in for loop

print("\n")
for x in range(6):
    print(x)
else:
    print("End of line")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finished")