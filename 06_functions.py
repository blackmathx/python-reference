# Bo Payton
# Python Language Reference - Functions



# function with argments and return value
def my_function(fname, lname):
	return fname + ' ' + lname

full_name = my_function("hank", "spore")
print(full_name)

# send arguments using key/value
full_name_2 = my_function(lname = "spore", fname = "hank")
print(full_name_2)


# pass statement because functions can't be empty
def my_other_fn(name):
	pass 

# arbitrary number of args, the argument type is 'tuple' and you can obtain the length
def my_function2(*kids):
	print("The youngest is " + kids[2])

my_function2("emil", "tobias", "lionel")


# any number of arguments, otherwise known as *kwargs in the docs. The argument type is 'dict'
def my_function3(**kid):
	print("last name is " + kid["lname"])

my_function3(fname = "hank", lname = "spore")


# default parameter value
def my_function4(country = "Norway"):
	print("from " + country)

my_function4() # if no input, the default value is used


# pass a list as an argument
def my_list_fn(food):
	print(*food, sep=', ') # unpacks the list. puts spaces if sep is not present
	print(' '.join(str(x) for x in food)) # another way to unpack the list using join

food = ['apple', 'corn chowder', 'french fries']
my_list_fn(food)


