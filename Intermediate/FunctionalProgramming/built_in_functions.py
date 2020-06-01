# Built in pure functions

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# map
def get_double(item):
  return item*2

print(list(map(get_double, list1))) # [2, 4, 6]

# filter
def get_odds(item):
  return item % 2 != 0

print(list(filter(get_odds, list1))) # [1, 3]

# zip
print(list(zip(list1, list2))) # [(1, 4), (2, 5), (3, 6)]
