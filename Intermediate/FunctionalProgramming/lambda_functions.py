# Lambda functions
from functools import reduce

# map using lambda functions
list1 = [1, 2, 3]
print(list(map(lambda item: item*2, list1))) # [2, 4, 6]

# reduce list
print(reduce(lambda acc, item: acc + item, list1, 0)) # 6
