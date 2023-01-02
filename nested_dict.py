"2 ways to create nested dicts"

#Eg 1.

familytree = {
    "father":{
        "name": "Bruce",
        "year": 1997
    },
    "mother": {
        "name": "Tahlia",
        "year": 1996
    },
    "child": {
        "name": "Damian",
        "year": 2012
    }

}

print(familytree)

#Eg 2.

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)