import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Formatting to make the string easier to read
# indent parameter
x = json.dumps(x, indent=4)
print(x)

# separators parameter
x = json.dumps(x, indent=4, separators=(". ", " = "))
print(x)

# sort_keys parameter
x = json.dumps(x, indent=4, sort_keys=True)
