import os # to delete you will need to import the OS module.

os.remove("demofile.txt")

# check if file exists first before deleting

if os.path.exists("demofile.txt"):
   os.remove("demofile.txt")
else:
  print("File does not exist")
