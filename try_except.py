"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
# Try and except error handling.
try:
  print(y)
except:
  print("Error occured")
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try and except is finished")
  
