"""
Dictionaries are ordered, unchangable and do not allow duplicates.

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(thisdict)

"Dictionary Length"

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict))

"The dict() constructor"

thisdict = dict(name = "John", age =  36, country = "Gotham")
print(thisdict)