#Lists allow duplicate values to be stored inside
fruitlist = ["apple","apple","apple","apple","apple"]
print(fruitlist)

#length of list 
print(len(fruitlist))

# use the method list() to create a list

batman = list(('apple','batman','food'))
print(batman)

# inserting items into  list using insert()
batman.insert(1, 'superman')
print(batman)

# extend list
catwoman = ['mango', 'papaya', 'arrow']
batman.extend(catwoman)
print(batman)

# pop() to remove the last item in the list
batman.pop()
print(batman)

# del() to delete specific index or the whole list clear() to clear the list.
del batman[-1]
print(batman)

del catwoman
