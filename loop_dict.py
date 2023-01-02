dct = {
    "model": 1999,
    "brand": "Microsoft",
    "name": "Windows"
}

for x in dct:
    print(x)
#prints all key names 1 by 1

for x in dct:
    print(dct[x])
#prints all values in dict 1 by 1

"Looping through both keys and values"

for x,y in dct.items():
    print(x,y)
#pritns both key and values side by side

"Copying dict using copy() method"

newdct = dct.copy()

print(newdct)

#or

"use dict() method"

newdct = dict(dct)
print(newdct)