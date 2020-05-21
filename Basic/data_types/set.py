# Set type
# It is an unordered unique element list

s1 = {1, 2, 3, 4, 5, 3, 2}
s2 = {11, 'str1', True, None, True, 11}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {11, 'str1', True, None}

# we can not set individual element a value
s3 = {1, 2, 3, 4, 5, 3, 2}
#s3[2] = 55 # error
#print(s3[2]) # error

# remove duplicates from list
l1 = [1, 2, 2, 3, 3, 3]
print(set(l1)) # {1, 2, 3}

# set methods
s4 = {1, 2, 3, 4, 5, 6}
s5 = {4, 5, 6, 7, 8, 9}

s4.discard(6)
print(s4) # {1, 2, 3, 4, 5}
print(s4.difference(s5)) # {1, 2, 3}
s4.difference_update(s5)
print(s4) # {1, 2, 3}
print(s4.intersection(s5)) # {4, 5}
print(s4 & s5) # {4, 5} shortcut for intersection
print(s4.isdisjoint(s5)) # False
print(s4.union(s5)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s4 | s5) # {1, 2, 3, 4, 5, 6, 7, 8, 9} shortcut for union

s6 = {4, 5}
s7 = {1, 2, 3, 4, 5, 6, 7}
print(s6.issubset(s7)) # True
print(s7.issuperset(s6)) # True

