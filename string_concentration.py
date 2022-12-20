"""String Concentration"""
#prints out HelloWorld
a = "Hello"
b = "World!"
c = a + b
print(c)

#adding space in between
c = a + " " + b
print(c)

"""String formatting"""
# format() method takes the passed arguements, formats them, and places them in strings where placeholders "{}" are.
# prints out My name is Bruce, I am 36
age = 36
txt = "My name is Bruce, I am {}."
print(txt.format(age))

quantity = 20
item = 2000
price = 50
myOrder = "I want to pay {2}, dollars for {0} pieces of item {1}"
#                      0        1      2
print(myOrder.format(quantity, item, price))


"""Escape Characters"""
# character \ before " and after " allows quotations inside the string.
txt = "We are \"Vikings\" of the north."

# for more of String Methods: https://www.w3schools.com/python/python_strings_methods.asp
