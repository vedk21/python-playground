# Tuple type
# They are very similar to list in python, but they are immutable in nature

t1 = (1, 2, 3, 4, 5)
t2 = (11, 'str2', True, [32, 45, 67], None)
print(t1[3]) # 4
print(t2[2]) # True

# we can not change the values in tuple or even change the order of the elements inside tuple

# unpacking tuple into list
x, y, *other, z = (1, 2, 3, 4, 5, 6)
print(x) # 1
print(y) # 2
print(other) # [3, 4, 5] 
print(z) # 6

# count
t3 = (1, 2, 3, 4, 5)
print(t3.count()) # 5

# index
t4 = (1, 2, 3, 4, 5)
print(t4.index(2)) # 1
