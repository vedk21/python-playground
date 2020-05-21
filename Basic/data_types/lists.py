# List type

l1 = [1, 2, 3, 4, 5, 6] # homogenous list
l2 = [1, 'str1', True, [2, 4, 'str2']] # heterogenous list

# Lists are mutable in nature
l1[2] = 10
print(l1) # [1, 2, 10, 4, 5, 6]
l2[1] = [4, 5, True]
print(l2) # [1, [4, 5, True], True, [2, 4, 'str2']]

# List slicing
l3 = [4, 5, 'str3', True, False]
l4 = l3[1:3]
print(l4) # [5, 'str3']
print(l3) # [4, 5, 'str3', True, False]

# List are reference typed
l5 = [1, 2, 3, 4, 5]
l6 = l5
l6[3] = 11
print(l6) # [1, 2, 3, 11, 5]
print(l5) # [1, 2, 3, 11, 5]

# Clone Copy list
l7 = ['box', 'computer', 'ball', 'bottle']
l8 = l7[:]
print(l8) # ['box', 'computer', 'ball', 'bottle'] (This will be the cloned copy and not referenced copy)
l7_7 = ['box', 'computer', 'ball', 'bottle']
l8_8 = l7_7.copy()
print(l8_8) # ['box', 'computer', 'ball', 'bottle'] (This will be the cloned copy and not referenced copy)

# Matrix list
m1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(m1[0][2]) # 3
print(m1[1]) # [4, 5, 6]

# Operations #

# Addition
l9 = [1, 2, 3, 4, 5]
l9.append(10)
print(l9) # [1, 2, 3, 4, 5, 10]
l9.insert(2, 101)
print(l9) # [1, 2, 101, 3, 4, 5, 10]
l9.extend([102, 103])
print(l9) # [1, 2, 101, 3, 4, 5, 10, 102, 103]
l9.insert(11, 105) # if index is greater than length od list, it will always insert at end of list
print(l9) # [1, 2, 101, 3, 4, 5, 10, 102, 103, 105]

# Removal
l10 = [1, 2, 3, 4, 5]
l10.remove(4)
print(l10) # [1, 2, 3, 5] (remove takes a value to be removed)
ele1 = l10.pop()
print(l10) # [1, 2, 3] (with no argument, removes last element and returns the element)
print(ele1) # 5
ele2 = l10.pop(1)
print(l10) # [1, 3] (removes element from given index and returns the element)
print(ele2) # 2
l10.clear()
print(l10) # []

# Index
l11 = ['a', 'b', 'c', 'd', 'e']
print(l11.index('b')) # 1
# limit the search
print(l11.index('b', 0, 3)) # 1 (it throws an error if not found in given range)

# Count
l12 = ['a', 'b', 'c', 'c', 'e']
print(l12.count('c')) # 2

# Sort
l13 = ['a', 'b', 'y' 'c', 'a', 'e']
l13.sort()
print(l13) # ['a', 'a', 'b', 'c', 'e', 'y']
l14 = ['a', 'b', 'y' 'c', 'a', 'e']
l15 = sorted(l14)
print(l15) # ['a', 'a', 'b', 'c', 'e', 'y']
print(l14) # ['a', 'b', 'y' 'c', 'a', 'e']

# Reverse
l16 = ['a', 'b', 'y' 'c', 'a', 'e']
l16.reverse()
print(l16) # ['e', 'a', 'c', 'y', 'b', 'a']
l17 = ['a', 'b', 'y' 'c', 'a', 'e']
print(l17[::-1]) # ['e', 'a', 'c', 'y', 'b', 'a'] (creates new reversed list)

# Generate list
print(list(range(101))) # [0, 1, 2, 3, ..., 99, 100]

# List unpacking
a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
print(c) # 3
w, x, y, *other, z = [1, 2, 3, 4, 5, 6, 7]
print(w) # 1
print(x) # 2
print(y) # 3
print(other) # [4, 5, 6]
print(z) # 7

# is present in list
l18 = ['a', 'b', 'c', 'd']
print('b' in l18) # True
print('x' in l18) # False
