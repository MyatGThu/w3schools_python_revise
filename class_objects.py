#Create a class
class myClass:
    x = 2023

#Create an object

p1  = myClass()
print(p1.x)

#Above examples are dog shit in real life projects as they are simple examples

# __init__() function

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = User("Jon", 22)

print(p1.name)
print(p1.age)

# __str()__ function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name},{self.age}" #f = f-strings (Format strings)

p1 = Person("Jack", 22)
print(p1)

#self parameter in class creation, to refrence an instance of class and used to access its variables

class Hero:
    def __init__(averagehero, name, age):
        averagehero.name = name
        averagehero.age = age
    
    def myfunc(asd):
        print("Hero name is " + asd.name)

p1 = Hero("Luke", 32)
p1.myfunc()