# Using error handling to close objects and clean up resources
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
# Raising exceptions
# 'raise' keyword , Exception() method
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
  
  
# TypeError() method

x = "batman"
if not type(x) is int:
  raise TypeError("Only intergers are allowed")
