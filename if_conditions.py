a = 1
b = 2

if b > a:
    print("b is greater")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

"and keyword"
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are true")

"or keyword"

if a > b or a > c:
    print("Only 1 condition is True")

#Nested if

x = 41

if x > 10:
    print("Above 10,")

    if x > 20:
        print("also above 20!")
    else: 
        print("not above 20.")

#if statements cannot be empty, put in 'pass' statement to avoid an error;

a = 33
b = 200
if b > a:
    pass

#short hand statements
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")