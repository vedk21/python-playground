# Dictionary type

d1 = {
  'a': 'str1',
  'b': 45,
  'c': True,
  'd': [1, 2, 3],
  'e': None
}
print(d1['c']) # True
print(d1['d']) # [1, 2, 3]
print(d1['d'][1]) # 2

# keys
# dictionary keys are immutable, so that they can be hashed
# keys has to be unique
d2 = {
  123: 'acceptable',
  True: 'acceptable',
  'str1': 'acceptable',
  [1, 2, 3]: 'not acceptable' # will throw an error
}

# check if key exists and get value
d3 = {
  'is_passed': True,
  'marks': [12, 34, 21],
  'name': 'Mark'
}
print(d3.get('name')) # Mark
print(d3.get('first_name')) # None
print(d3.get('first_name', 'Key not present')) # Key not present

# create dictionary using dict() method
d4 = dict(name='Mark', age=23)
print(d4)

# check if key is present in dictionary
d5 = {
  'a': 'str1',
  'b': 45,
  'c': True
}
print('a' in d5) # True
print('x' in d5) # False
print('x' in d5.keys()) # False
# doing ('a' in d5) and ('a' in d5.keys()) is same
# we can also look in values
print('str1' in d5.values()) # True
print(False in d5.values()) # False
# get the complete key:value pair in an tuple
print(d5.items()) # dict_items([('a', 'str1'), ('b', 45), ('c', True)])

# Clear
d6 = {
  'a': 'str1',
  'b': 45,
  'c': True
}
d6.clear()
print(d6) # {}

# clone copy
d7 = {
  'a': 'str1',
  'b': 34
}
d8 = d7.copy()
d7.clear()
print(d7) # {}
print(d8) # {'a': 'str1', 'b': 34}

# pop
d9 = {
  'a': 'str1',
  'b': 34
}
print(d9.pop('b')) # 34
print(d9) # {'a': 'str1'}

# update
d10 = {
  'a': 'str1',
  'b': 34
}
d10.update({'b': 40})
print(d10) # {'a': 'str1', 'b': 40}
d10.update({'c': 21})
print(d10) # {'a': 'str1', 'b': 40, 'c': 21}
