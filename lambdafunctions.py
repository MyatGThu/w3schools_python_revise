#An anonymous function inside another function

#lambda arguements : expression
x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5,8))

def myfunction(n):
    return lambda a: a * n

doubler = myfunction(2)

print(doubler(11))
