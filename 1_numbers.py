# Bo Payton 9/11/23
# Python Language Reference - Numbers


# booleans
print(False)
print(bool(1)) # true, any non-zero is  true
print(bool(0)) # false, any 0 is false including 0.0
print(bool('st')) # True


# numbers
million = 1_000_000 # valid, underscores are ignored
million_v2 = 1,000,000 # not valid, produces a tuple (1, 0, 0)
print(5 // 2) # floor division, throw away the remainder so equals 2
print(5 % 2) # modulo, prints remainder 1
print( 2 ** 3) # ** is power operator, 2^3 is 8


# bases
# 0b or 0B for binary, 0o or 0O for octal, 0x or 0X for hex
print(0b10) # prints 2
print(bin(2)) # prints 0b10
print(0o10) # prints 8
print(oct(8)) # prints 0o10
print(0x41) # prints 65
print(hex(65)) # prints 0x41
# if a string is a nondecimal integer you can include the base
print(int('10', 2)) # binary, 2
print(int('10', 8)) # octal, 8
print(int('10', 16)) # hex 16


# character
print(chr(65)) # prints single character string which is 'A'
print(ord('A')) # prints the opposite, so 65

# type conversions
print(int(True)) # 1
print(int(98.6)) # prints 98
# print(int('98.6')) # invlaid!!!!
print(int(1.0e4)) # prints 1000
# print(int('1.0e4')) # invalid!!!!
abc = int('99') # 99
defg = int('+12') # 12
hij = int('1_000') # 1000
print(4 + 7.0) # prints 11.0

# float
print(float(True)) # 1.0
print(float('98.6')) # 98.6
print(float('1.0e2')) # 100.0
k = 4 + 2.0 # promotes to float
l = True + 1 # 2, promotes booleans to integers or floats


# math
# TODO







