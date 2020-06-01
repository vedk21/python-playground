# List comprehensions (easy way to create lists in python)

list1 = [num for num in range(0, 5)]
print(list1) # [0, 1, 2, 3, 4]

list2 = [num*2 for num in range(0, 5)]
print(list2) # [0, 2, 4, 6, 8]

list3 = [num for num in range(0, 5) if num % 2 == 0]
print(list3) # [0, 2, 4]

# Set comprehensions (easy way to create sets in python)
set1 = {num for num in range(0, 5)}
print(set1) # {0, 1, 2, 3, 4}

set2 = {num*2 for num in range(0, 5)}
print(set2) # {0, 2, 4, 6, 8}

set3 = {num for num in range(0, 5) if num % 2 == 0}
print(set3) # {0, 2, 4}

# Dictionary comprehensions (easy way to create dictionary in python)
tup = [('hi', 1), ('hey', 2)]
dict1 = {key:value for key, value in tup}
print(dict1) # {'hi': 1, 'hey': 2}

dict2 = {key:value*2 for key, value in tup}
print(dict2) # {'hi': 2, 'hey': 4}
