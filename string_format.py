# format() method
# {} is a place holder for specified variable / setter.

price = 49
txt = "The price is {} dollars. "

print(txt.format(price))

# using parameters 
txt = "The price is {:.2f} dollars. " #prints out to 2 decimal places

# using multiple placeholders
quantity = 4
itemno = 1000
price = 50
myOrder = "I want {} pieces of item number {} for {:.2f} dollars. "
print(myOrder.format(quantity, itemno, price))


