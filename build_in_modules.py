#importing build in platforms

import platform

x = platform.system()

print(x)

x = dir(platform)
print(x) #prints out defined names belonging to the module

# Importing parts of a module

from newmodule import person1

print(person1["age"])