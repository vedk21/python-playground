# string type
st1 = "double quotes string"
st2 = 'single quotes string'
st3 = '''Multi
line string
'''
# string concatenation
print('first' + 'second') # 'firstsecond'

# type conversion
st4 = str(400) # '400'

# Escape characters
st5 = "I am writing double quote \" inside string" # 'I am writing double quote " inside string'
st6 = "\tThis line is tabbed\nThis line is on new line" # \t -> tab, \n -> new line

# formatted strings
name = 'Jack'
age = 23
print(f'My name is {name}. I am {age} year\'s old') # 'My name is Jack. I am 23 year's old'

# string indexes
st7 = 'abcdef'
print(st7[4]) # 'e'
# [startIndex : endIndex : stepOver]
# endIndex is excluded from range
print(st7[1:4]) # 'bcd'
print(st7[1:]) # 'bcdef'
print(st7[:4]) # 'abcd'
print(st7[0:5:2]) # 'ace'
print(st7[-1]) # 'f'
print(st7[-3]) # 'd'
print(st7[::-1]) # 'fedcba'
