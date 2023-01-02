#Creating a function


#defines a fucntion
def new_func():
    print("Hello from a function")

#calling a function
new_func()

#arguements

def my_function(fname):
    print(fname + " Wayne")

my_function("Nova")
my_function("Linus")
my_function("Tobias")

"""
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#satisfying only 1 arguements gets an error e.g. my_function("Emil")

"Arbitrary Arguements, *args"

def myfunction(*kids):
    print("Youngest child is " + kids[1])

myfunction("Bruce", "Anthony", "Saka")

#Keyword Arguements

def myfucntion(child3, child2, child1):
    print("Child is " + child3)

myfucntion(child3= "Linus", child1="Bruce", child2="Ace")

"Keyword arguements **kwargs"

def myfunction(**kids):
    print("His last name is " + kids["lname"])
myfunction(fname = "Toby", lname = "Genish")

#Default parameter value

def my_function(country = "Myanmar"):
    print("I am from " + country)

my_function("Sweden")
my_function("Iceland")
my_function() #prints out the default value specified in the parameter
my_function("Cambodia")


#Passing a list as an Arguement

def new_fun(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "grapes"]

new_fun(fruits)

#Return Values

def fun_end(x):
    return 5 * x

print(fun_end(4))
print(fun_end(5))
print(fun_end(7))
