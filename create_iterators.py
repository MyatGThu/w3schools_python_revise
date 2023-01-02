# Creating a object/class iterator.
class myNum:
  def __inter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = myNum()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stopping iterations to avoid continuous loop

class MyNumber:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      return x
    else:
      raise StopIteration # Without this statement, the loop will run forever printing out None.
mClass = MyNumber()
miter = iter(myclass)

for x in miter:
  print(x)
