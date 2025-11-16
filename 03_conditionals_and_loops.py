
# Python Language Reference - Conditionals and Loops


########## if-else, elif
if 1 > 2:
    print('1 > 2')
else:
    print('1 < 2')


color = 'RED'
if color == 'Blue':
    print('blue')
elif color == 'Green':
    print('green')
else:
    print('RED')



########## swap variables
a = 4
b = 5
a,b = b,a 
print(a, b) # prints 5 4

########## === in Python checks if equal by datatype and value
# TODO



########## logical operators
if (True and True):
    print('t') # prints 't'
if True and True:
    print('t') # prints 't'
if not False:
    print('t') # prints 't'
if (not False):
    print('t') # prints 't'
if (0 or 1):
    print('t') # prints 't'
if 0 | 1:
    print('t') # prints 't'



########## is, is not
if 0 is False: # is. checks if two values are located on the same part of memory. equals does not imply identical
    print('t') # prints 't'
if 0 is not True: # is not. checks if values are not identical
    print('t') # prints 't'
x1 = 5
x2 = 5
if x1 is x2:
    print('t') # prints 't'
y1 = 'Hello'
y2 = 'Hello'
if y1 is y2:
    print('t') # prints 't'
z1 = [1, 2, 3]
z2 = [1, 2, 3]
if z1 is z2:
    print('t') 
else:
    print('f') # prints 'f'



########## in, not in
# test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary)
m = [1, 2, 3] # list
n = {1:'a', 2:'b'} # dictionary
if 3 in m:
    print('t') # prints 't'
print('t') if 'a' in n else print('f') # check if a key is present in n, it is not
if 1 in n:
    print('t') # prints 't'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print('t') if 'e' in vowel_set else print('f') # prints 't'
vowel_string = 'aeiou' # could have used "aeiou"
print('t') if 'o' in vowel_string else print('f') # prints 't'
print('sdf' * 3) # prints 'sdfsdfsdf'
print(len('sdfsd')) # prints 5


########## ternary
print('fun') if 1 < 2 else print('not fun') # prints fun


