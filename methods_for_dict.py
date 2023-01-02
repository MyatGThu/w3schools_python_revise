thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "model": "Mustang"
}

x = thisdict["model"]

"the get() method"

x = thisdict.get("model")

"the keys() method"

x = thisdict.keys()

"Modifying dictionary"

car = {
    "brand": "Rolls",
    "model": "RU",
    "year": 2000
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)


"the values() method"

x = car.values()
print(x)

"the items() method"

x = car.items() #prints everything stored in the dictionary as a tuples including the keys.
print(x)

"the update() method"

car.update({"year": 2021})
print(car)

"popitem() method"

#removes the last inserted item
car.popitem()
print(car)

"del keyword"

#del keyword removes the either the specified key name or the dict completely
del car['brand']
print(car)

"del car  print(car) #this will result in an error"

"clear() method"

#empties the dict

car.clear()
print(car)
