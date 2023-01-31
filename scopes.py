""" 
Variables inside a function is only available inside that function, i.e. local scope.
A variable is not available outside the function but is available for any function,
inside the function.
"""

# Local scope fucntion e.g.

def myfunc():
  x = 30
  def myinnerfunc(): #calling variable inside function.
    print(x)
  myinnerfunc()

myfunc()

# Global scope function e.g.

x = 3000
def myfunc():
  x = 200
  print(x)

myfunc() #prints internal defined x = 200
print(x) #prints global 3000.

# Creating a global variable using 'global' keyword inside a local function.

def myfunc():
  global y
  y = 4000

myfunc()
print(y)

# Change the gloabl variable from a local function.

x = 300

def myfunc():
  global x
  x = 200
myfunc() # prints out 200

print(x) # changes the variable outside the function to 200.
