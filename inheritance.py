"""
Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""

#creating a parent class,

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Jack", "Danger")
x.printname()

#creating a child class

class Student(Person):
    def __init__(self,fname,lname, year):
        super().__init__(fname,lname) #using super() function replaces this Person.__init__(self,fname,lname) 
        self.graduationyear = year #adding properties to child class. you will also have to add to the parameters
    
    def welcome(self):
        print("Welcome, ", self.firstname, self.lastname, "to the class of ", self.graduationyear)

x = Student("Mike", "Donger", 2019)
x.welcome()

