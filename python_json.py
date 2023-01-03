import json

# Converting JSON strings to Py

x = '{ "name": "John", "age": 30, "city": "New York"}'

# use the loads() method from the imported json module
# parse x
y = json.loads(x)

# results in Python dicts. 
print(y["age"])

# Converting Py objects to JSON

x = {
  "name": "Jack",
  "age": 25,
  "city": "Melbourne"
}

y = json.dumps(x)

print(y)

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
"""

