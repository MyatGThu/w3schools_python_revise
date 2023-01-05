f = open("demofile.txt", "a") # "a" adding to the end of the file

f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")

f = open("demofile.txt", "w")
f.write("Woops! There goes the content")

f.close()

f = open("demofile.txt", "r")
print(f.read())
