x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

""" global keyword """
def myfun():
    global x
    x = "fantastic"

myfun()
print("Python is " + x)


