
# Python Language Reference - Files and Directories

import os
import time



f = open(".gitignore", "r") # returns a file object
contents = f.read() # read the file into a variable
f.close()


# read two lines of the file
g = open("01_numbers.py", "r")
print(g.readline())
print(g.readline()) 
g.close()


# loop through the file line by line
h = open("03_strings.py", "r")
for x in h:
	print(x)
h.close()



# write to a file, add 'a' to append or 'w' to overwrite
i = open("demo.txt", "a")
i.write("testing\ntwo")
i.close()
j = open("demo.txt", "r")
print(j.read())
j.close()


### mode values for open()
# "r" - Open a file for reading. (default)
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
# 't' - Open in text mode. (default)
# 'b' - Open in binary mode.
# '+' - Open a file for updating (reading and writing)

#### other parameters for open()
# mode (optional) - mode while opening, if not provided it defaults to 'r' for reading
# buffering (optional) - used for setting buffering policy
# encoding (optional) - the encoding format
# errors (optional) - string specifying how to handle encoding/decoding errors
# newline​ (optional) - how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'


time.sleep(1) # adding a delay to see demo.txt created from above before deleting it



# delete a file with
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
else:
  print("The file does not exist") 



# delete a folder with 
try:
	os.rmdir("myfolder")
except:
     print("The folder does not exist")


