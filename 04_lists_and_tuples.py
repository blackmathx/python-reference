'''
04_lists_and_tuples.py

'''

########## Lists

furniture = ['table', 'chair']
length = len(furniture) # length function
a = furniture[0] # access index 0
furniture[-1] = 'bed' # change end item to 'bed'
list_2 = ['dresser', 'rack', 'shelf', 'chair']
furniture = furniture + list_2 # concatiante lists
furniture.append('recliner') # append item
furniture.insert(1, "desk") # insert into index
furniture.remove('recliner') # remove item
furniture.pop(0) # pop an index
furniture.pop() # pop from the end
del furniture[-1] # delete by index
print(furniture[0:2]) # prints items 0 and 1
print(furniture[1:]) # prints everything except 0 element
print(sorted(furniture)) # prints items sorted, sorted returns a new list
furniture.sort()
furniture.reverse() # reverse corrent order
fur2 = furniture.copy() # copy method to make a copy of a list
fur3 = list(furniture) # another way to copy a list
fur4 = furniture + fur2 # join lists
fur4.extend(fur3) # append elements to a list
num = fur4.count('dresser') # count the number of occurances
print( num)
for z in range(len(furniture)):
	print(furniture[z])
for x in furniture:
	print(x)
k = 0 
while k < len(furniture):
	print(furniture[k])
	k += 1
[print(x) for x in furniture] # loop this way is called comprehension
for item in furniture:
	print(f'item: {item}')

if 'rack' in furniture:
	print('t')
else:
	print('f') # prints 'f'
furniture.append('shelf')
del furniture[1] # removes element and shortens by one
furniture.clear() # clear everything from the list
del furniture # delete the list completely


########## Tuples

# tuples are immutable, like strings, convert to list, update, then convert back to change it
fruits = ("apples", "bananas", "cherries")
pink = tuple(fruits) # converts a list to a tuple
green = list(pink) # converts a tuple to a list
yellow = list('hello') # converts a string to a list ['h', 'e', 'l', 'l', 'o']
(green, yellow, red) = fruits # unpack the tuple into variables
for y in fruits:
	print(y)
for i in range (len(fruits)):
	print(fruits[i])
veggies = ("carrots", "corn")
food = fruits + veggies # join tuples with +
food2 = food * 2 # duplicate the items in the tuple
occur = food2.count("corn") # count() returns the number of times the value occurs