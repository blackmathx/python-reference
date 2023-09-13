# Bo Payton 9/11/23
# Python Language Reference - Lists, Tuples, Dicts, Sets


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
(green, yellow, red) = fruits # unpack the tuple into variables!
for y in fruits:
	print(y)
for i in range (len(fruits)):
	print(fruits[i])
veggies = ("carrots", "corn")
food = fruits + veggies # join tuples with +
food2 = food * 2 # duplicate the items in the tuple
occur = food2.count("corn") # count() returns the number of times the value occurs





########## Dictionaries

# dictionary is an ordered (Py > 3.7) colleciton of 'key':'value' pairs
my_cat = {'size':'fat', 'disposition':'loud'}
my_cat['age'] = 5 # set key, value with brackets
for value in my_cat.values():
	print(value)
for key in my_cat.keys():
	print(my_cat[key]) # using keys
for key in my_cat:
	print(key) # loops over keys
for key, value in my_cat.items():
	print(f'Key:{key}, Value:{value}')
print(my_cat.get("size"))
if 'hair' not in my_cat:  
	my_cat['hair'] = True # add items
print(my_cat.pop('hair')) # pop an element. returs the value and removes it
print(my_cat.popitem()) # popitem() removes the last element and returns it ('age', 5) will be returned
del my_cat['disposition'] # delete item
my_cat.clear() # removes all items in the dictionary
my_bool = 'age' in my_cat.keys() # returs False
my_cat['age'] = 5
my_bool2 = 5 in my_cat.values() # returns True
dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
dict_c = {**dict_a, **dict_b} # merge two dictionaries (Python 3.5+)


########## Sets

# a set is an unordered collection with no duplicate elements, sets are immutable but you can add and remove items
# initialize a set in two ways, using {} and using set()
set_a = {1, 2, 3, 4} # init a set
set_b = set(("apple", "banana", "cherry")) # init a set
set_c = {True, 'chair', 1, 2, 3} # 1 is the same as True so the duplicate will be ignored, can containe different types. {True, 2, 3, 'chair'}
length = len(set_c)
print(type(set_a)) # <class 'set'>
set_d = {} # this creates a dictionary instead of a set, <class 'dict'>
#print(set_a[0]) # invalid!!! sets don't support indexing
set_a.add(5)
for x in set_a:
	print(x)
set_a.remove(2) # removes element, but invalid if doesn't exist!!!!! use discard() will not raise an error
set_a.discard(100) # discard() removes but doesn't raise an error
set_e = set_a.union(set_b) # union is sale as update() 
set_f = set_a.intersection(set_c) # intersection
set_g = set_a.difference(set_c) # a minus c
set_h = set_a.symmetric_difference(set_c) # returns elements not common between them
set_a.update(set_c) # add elements of set_c to set_a
set_a.update(['zyx', 'cdefg']) # update() works with any iterable including lists
set_a.intersection_update(set_c) # keep only the duplicates in set_a
set_a.symmetric_difference_update(set_c) # keep only elements not present in both sets
set_a.symmetric_difference_update(set_c) # keep items not present in both sets
print(set_a.pop()) # returns and removes a random item!!!!
set_a.clear() # clears everything form the set
del set_a # deletes the set completely



