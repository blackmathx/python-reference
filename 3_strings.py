# Bo Payton 9/11/23
# Python Language Reference - Strings


########## quick notes
poem = '''this is a 
multiline string'''
print('Give', "us", '''some''', """space""") # prints each with a space between
var_10 = str(1.03e4) # '10300'
print(str(True)) # prints 'True'
var_20 = str(98.6) # '98.6'
# escape new line and tab with \n or \t
print('her\'s') # prints 'her's'
print('his \\') # prints 'his \'
info = r'Type a \n to get a new line ' # an r string negates escapes
poem_2 = r'''Boys and girls
come out to play'''
print(poem_2) # prints 'Boys and girls\ncome out to play


########## concatinate
print('release the kraken. ' + 'no wait!') # concat

########## string manipulation
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[5]) # f
print(letters[-1]) # z
print(letters[-2]) # y
#letters[5] = 'j' # invalid!!!! strings are immutable
letters.replace('f', 'j') # now it's replaced but it doesn't change letters
letters = letters.replace('a', 'z') # now a is replaced with z
print('ABC' + letters[3:]) # prints 'ABCdefg...'


########## slice
letters[:] # extracts entire sequence start to end
letters[2:] # from position 2 to end
letters[:20] # from start to position 20
letters[1:3] # from position 1 to 3 minus 1 so 'bc'. doesn't include the end position
letters[0:20:2] # from 0 to 20, step by 2. [start:end:step]
letters[19::3] # from 19 to end step by 3
letters[-3:] # -3 positon to end
print(len(letters)) # 26

########## split
tasks = 'get gloves, get mask,give cat vitamins,visit ann'
list_1 = tasks.split(',') # provides list split on ','
list_2 = tasks,split() # provides list split on spaces, newlines or tabs, ie any whtiespace characters

########## join
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list) # joins elements of the list with ', '

########## substitute and replace
setup = 'a duck goes into a bar..'
setup.replace('duck', 'marmoset')
setup.replace('a ', 'a famous ', 100) # change upto 100 of them
setup.replace('a ', 'a famous ') # change them all

########## strip
world = "    earth   "
print(world.strip()) # strips whitespace characters from both ends
print(world.lstrip()) # left strip
print(world.rstrip()) # right strip
print(world.strip(' ')) # strips only spaces from both ends
blurt = 'what the...!!?'
print(blurt.strip('.?!')) # prints 'what the'

########## search and select
poem_3 = "All that doth flow we cannot liquid name"
print(poem_3.startswith('All')) # prints 'True'
print(poem_3.endswith('name')) # prints 'True'
word = 'we'
print(poem_3.find(word)) # prints 19
print(poem_3.index(word))
print(poem_3.find('moreover')) # prints -1, not found
print(poem_3.index('moreover')) # invalid!!!! no index found
print(poem_3.count(word)) # prints count of 1
print(poem_3.isalnum()) # prints if it's all alpha numeric, so True

########## case
duck = 'a duck goes quack'
duck.capitalize() # cap the first word
duck.title() # cap all words
duck.upper() # all to uppercase
duck.lower() # all to lowercase
duck.swapcase() # swap all cases




# f strings
# TODO