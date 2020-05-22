# For loop

for item in [1, 2, 3, 4, 5]:
  print(item)

for ch in 'hey there!!!':
  print(ch)
print(ch) # will print last character from string, this is valid in python

# iterables
# list, tuple, set, dictionary, string
d1 = {
  'name': 'Mark',
  'age': 24,
  'is_user_valid': True
}
for item in d1:
  print(item) # prints keys of the dictionary
# same as above
for item in d1.keys():
  print(item) # prints keys of the dictionary
# print only values
for item in d1.values():
  print(item) # prints values of the dictionary
# print tuple of key and value
for item in d1.items():
  print(item) # prints tuple(key, value) of the dictionary
# shortcut for above
for k, v in d1.items():
  print(k, v) # unpacks keys and values of the dictionary
