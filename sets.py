"""
Sets - 

Unchangable, but can remove / add items
{} is the symbol for sets.
Does not allow duplicates.
Similar to list / dict / tuples

"""
#looping sets.

aset = {'yegyi', 'minminzaw', 'kenee'}

for sawshi in aset:
    print(sawshi)

print('Ngelay' in aset) #boolean 

#add() method to add new items to sets.

aset.add('wukyi')
print(aset) #Unordered, will print out alphabetically

"Adding sets updated() method"

sawmashi = {'myathtu', 'zanboot', 'ngelay'}
sawmashi.update(aset)

print(sawmashi)

"Removing items in set"

thisset = {"apples", "coke", "html"}
thisset.remove("apples")

print(thisset) #will print out an error if item is 404

thisset.discard("apples")
print(thisset) #does not cause an error if there is no item

#similar to list() , pop() can be used to remove items along with del() methods

"Update()"
#adds a set into an existing set.

set1 = {"a", "b", "c"}
set2 = {1,2,3,4}
set1.update(set2)

print(set1)

"Union()"
#adds all items of a set tgt.
set3 = set2.union(set1)
print(set3)

"Intersection_update()"
#only add in duplicate
 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

"intersection()"
#only return item containing in both set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

"symmertirc_difference_update()"
#only keeps items not present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

y.symmetric_difference_update(x)

print(y)

"symmetric_difference()"
#keeps item present in both set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.symmetric_difference(x)
print(z)