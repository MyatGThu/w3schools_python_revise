i = 1
while 1 < 6:
    print(i)
    if i == 3: #rember to break the loop or it goes on 
        break
    i += 1

print("\n")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue #to stop current iteration and continue to the next
    print(i)
    
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")